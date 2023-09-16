from time import sleep
from mechanize import UserAgent
from src.collections.crypto_punks import CryptoPunks
from src.notificator import Telegram
from opensea import OpenseaAPI
from datetime import datetime 
from fake_useragent import UserAgent
import requests
import pandas as pd

class OpenSea: 

    telegram : Telegram

    def __init__(
        self, 
        api_key: str,
        **kwargs) -> None:
        
        self._main(api_key, **kwargs)

    def retrieve_assets(self):

        try:
            return self.client.assets(
                asset_contract_address=self.asset_contract_address
            )
        except Exception as _:
            return _

    def retrieve_asset(self, token_id: str):

        try:
            return self.client.asset(
                asset_contract_address=self.asset_contract_address,
                token_id=token_id
            )
        except Exception as _:
            return _
         
    def _collection(self): 

        self.collection = CryptoPunks()

    def _init(self, api_key: str, **kwargs):
        
        assert (
            api_key != "YOUR_API_KEY"
        ), "Need OpenSea Api." \
            " For further informations: " \
            "https://docs.opensea.io/reference/request-an-api-key."
        self.collection_slug = kwargs['collection_slug'] if (
            'collection_slug' in kwargs
        ) else None 
        self.asset_contract_address = kwargs['asset_contract_address'] if (
            'asset_contract_address' in kwargs
        ) else None
        assert (
            self.collection_slug != "COLLECTION_SLUG" or 
            self.collection_slug != None
        ), "Need a Collection slug."
        assert (
            self.asset_contract_address != "ASSET_CONTRACT_ADDRESS" or 
            self.asset_contract_address != None 
        ), "Need an Asset contract address."
        base_url = "https://testnets-api.opensea.io/api" if (
            'test' in kwargs and 
            kwargs['test']
        ) else "https://api.opensea.io/api"
        self.client = OpenseaAPI(
            base_url=base_url, 
            apikey=api_key
        )
        self.telegram = kwargs['telegram'] if (
            kwargs['telegram'] != None 
        ) else None # exit("Need Telegram.")

        #self._collection()
        #self.build_collection()
        #self.retrieve_listing()

    def retrieve(self):

        ids = self.score.iloc[0:, 0].values.tolist()
        self.toreset = []
        start = datetime.now() 
        for i in range(ids.__len__() - 1, 0, -1):
            res = self.client.events(
                self.collection.asset_contract_address, 
                self.collection.collection_slug, 
                token_id=ids[i],
                event_type='created',
                only_opensea=False
            )
            asset_event = res['asset_events']
            if (asset_event):
                totake = asset_event[0]
                try:                              
                    created_date = datetime.fromisoformat(totake['created_date'])
                    rank = self.score.loc[self.score['id'] == i].index.values.tolist()[-1]
                    score = self.score.loc[self.score['id'] == i]['score'].values.tolist()[-1]
                    now = datetime.now()
                    price = int(totake['ending_price'])
                    
                    price = price / 1000000000000000000 if (
                        price / 1000000000000000000 < 200
                    ) else price / 1000000000000000000
                    difference = (now - created_date).total_seconds()
                    print(now, created_date, difference)
                    if (difference < 7200):
                        if (self.toreset):
                            if (not (rank, price) in self.toreset):
                                self.toreset.append((rank, now, price))
                                m = 'Crypto Punk #{} listed.\n'\
                                    'Price: {} ETH.\n'\
                                    'Ranking: {}.\n'\
                                    'Score: {}'.format(
                                        ids[i],
                                        price, 
                                        rank,
                                        round(score, 2)
                                    )
                                if (self.telegram != None):
                                    self.telegram.send_message(m)
                            else:
                                pass 
                        else:
                            self.toreset.append((rank, now, price))
                            m = 'Crypto Punk #{} listed.\n'\
                                'Price: {} ETH.\n'\
                                'Ranking: {}.\n'\
                                'Score: {}'.format(
                                    ids[i],
                                    price, 
                                    rank,
                                    round(score, 2)
                                )
                            if (self.telegram != None):
                                self.telegram.send_message(m)
                except TypeError:
                    pass
            sleep(0.1)
        end = datetime.now() 
        time = end - start
        print(time)
  
    def retrieve_listing(self):
        
        self.start = datetime.now()

        while (True):
            
            self.retrieve()

            now = datetime.now()

            if ((now - self.start).seconds >= 8640):
                self.toreset = []

    def build_collection(self):

        x = 0
        y = x + 999

        self.score_collection = pd.DataFrame(columns=['id', 'score'])

        while (x <= 9000 and y <= 9999):

            temp = pd.read_csv('/Users/giuseppefiengo/documents/github/nft-notificator/src/collections/crypto_punks/{}-{}.csv'.format(x, y))

            for i in range(0, temp.__len__(), 1):

                data = temp.iloc[i, [0, 1, 2, 3, 4, 5]].values
                id = data[0] 
                type = data[1]
                gender = data[2]
                skin_tone = data[3]
                count = data[4]
                tempattr = data[5]
                attributes = self.attributes_to_list(tempattr)       
                score = self.find_attributes(attributes)
                type = self.remove_all_extra_spaces(type)
                gender = self.remove_all_extra_spaces(gender)
                skin_tone = self.remove_all_extra_spaces(skin_tone)
                score += self.punk_type_score(type, gender)
                score += self.full_type_score(skin_tone, gender, type)
                score += self.attributes_count_score(count)
                tempt = pd.DataFrame([[id, score]], columns=['id', 'score'])
                self.score_collection = pd.concat([self.score_collection, tempt], ignore_index=True)

            x = y + 1
            y = x + 999

        self.score_collection = self.score_collection.sort_values(by=['score'])
        index = [x for x in range(10000, 0, -1)]
        self.score = pd.DataFrame(self.score_collection)
        self.score.index = index 
        self.score.to_csv('scores.csv')

    def attributes_count_score(self, count: int):

        score = 0
        for general in self.collection.general.attribute_count.objects:
            if (general.value == str(count)):
                score = general.score
        return score 

    def full_type_score(self, skin_tone: str, gender: str, type: str):
        score = 0
        for general in self.collection.general.full_type.objects:
            if (general.value == '{}-{}'.format(gender, skin_tone)):
                score = general.score 
        if (score == 0):
            for general in self.collection.general.full_type.objects:
                if (general.value == type):
                    score = general.score 
        return score 

    def gender_type_score(self, gender: str):
        score = 0
        for general in self.collection.general.punk_type.objects:
            if (general.value == gender):
                score = general.score
        return score

    def punk_type_score(self, type: str, gender: str):

        score = 0

        for general in self.collection.general.punk_type.objects:
            if (general.value == type):
                score = general.score
        if (score == 0): 
            for general in self.collection.general.punk_type.objects:
                if (general.value == gender):
                    score = general.score
        return score

    def skin_tone_score(self, skin_tone: str):

        score = 0

        for general in self.collection.general.skin_tone.objects:
            if (general.value == skin_tone):
                score = general.score 
        return score 

    def remove_all_extra_spaces(self, string: str):
        return " ".join(string.split())

    def find_attributes(self, attributes: list):

        score = 0

        score += self.find_hair(attributes)
        score += self.find_eyes(attributes)
        score += self.find_facialhair(attributes)
        score += self.find_neckaccessory(attributes)
        score += self.find_mouth_prop(attributes)
        score += self.find_mouth(attributes)
        score += self.find_blemishes(attributes)
        score += self.find_ears(attributes)
        score += self.find_nose(attributes)
        return score 

    def find_hair(self, attributes: list): 

        hair = self.collection.attributes.hair 

        found = False 
        for __ in attributes:
            for _ in hair.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break 
            if (found):
                break
        if (not found):
            score = hair.none.score

        return score 

    def find_eyes(self, attributes: list):

        eyes = self.collection.attributes.eyes

        found = False 
        for __ in attributes:
            for _ in eyes.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break 
            if (found):
                break
        if (not found):
            score = eyes.none.score
        return score 
    
    def find_facialhair(self, attributes: list):

        facialhair = self.collection.attributes.facial_hair

        found = False 
        for __ in attributes:
            for _ in facialhair.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break 
            if (found):
                break 
        if (not found):
            score = facialhair.none.score
        return score 

    def find_neckaccessory(self, attributes:list):

        neckaccessory = self.collection.attributes.neck_accessory

        found = False 
        for __ in attributes:
            for _ in neckaccessory.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break 
            if (found):
                break
        if (not found):
            score = neckaccessory.none.score
        return score 

    def find_mouth_prop(self, attributes: list): 

        mouth_prop = self.collection.attributes.mouth_prop

        found = False 
        for __ in attributes:
            for _ in mouth_prop.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break
            if (found):
                break
        if (not found):
            score = mouth_prop.none.score

        return score 

    def find_mouth(self, attributes: list):

        mouth = self.collection.attributes.mouth

        found = False 
        for __ in attributes:
            for _ in mouth.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break
            if (found):
                break
        if (not found):
            score = mouth.none.score

        return score 

    def find_blemishes(self, attributes: list):

        blemishes = self.collection.attributes.blemishes

        found = False
        for __ in attributes: 
            for _ in blemishes.objects:
                if (_.value == __):
                    score = _.score
                    found = True 
                    break
            if (found):
                break 
        if (not found):
            score = blemishes.none.score

        return score 

    def find_ears(self, attributes: list):
        
        ears = self.collection.attributes.ears
    
        found = False 
        for __ in attributes:
            for _ in ears.objects:   
                if (_.value == __):
                    score = _.score
                    found = True 
                    break
            if (found):
                break
        if (not found):
            score = ears.none.score

        return score 

    def find_nose(self, attributes: list):

        nose = self.collection.attributes.nose

        found = False 
        for __ in attributes:
            for _ in nose.objects: 
                if (_.value == __):
                    score = _.score
                    found = True 
                    break
            if (found):
                break
        if (not found):
            score = nose.none.score

        return score

    def attributes_to_list(self, attributes: str):

        attributes_ = []

        s = ''
        for c in attributes:
            if (c != '/'):
                s += c 
            else: 
                attributes_.append(s)
                s = ''
            #print(str(attributes).index(c), str(attributes).__len__() - 1)
            #if (str(attributes).index(c) == str(attributes).__len__() - 1):
            #    attributes_.append(s)
            #print(s)
        attributes_.append(s)

        for i in range(0, attributes_.__len__(), 1):

            attributes_[i] = self.remove_all_extra_spaces(attributes_[i])

        return attributes_

    def _main(self, api_key: str, **kwargs): 

        self._init(api_key, **kwargs)
        self.collection_slug = "tiny-dinos-eth"
        self.asset_contract_address = "0xd9b78A2F1dAFc8Bb9c60961790d2beefEBEE56f4"
        #x = self.client.collection_stats(self.collection_slug)
        #y = self.client.collection(self.collection_slug)
        #m = self.client.contract()
        j = self.client.asset(self.asset_contract_address, 2921)

        #print(j)

        h = self.client.events()
        print(h)

        #print(self.asset_contract_address)

        #res = self.client.asset_listing(self.asset_contract_address, 2154)
        #print(res)