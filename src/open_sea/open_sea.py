from src.collections.crypto_punks import CryptoPunks
from src.notificator import Telegram
from opensea import OpenseaAPI
from datetime import datetime 

class OpenSea: 

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

    def _main(self, api_key: str, **kwargs): 

        self._init(api_key, **kwargs)