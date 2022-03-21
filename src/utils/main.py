from src.utils import read_file
from src.notificator import Telegram
from src.open_sea import OpenSea

def _main(config_path: str=None):

    configurations = read_file(config_path)

    notification = configurations['Telegram']['Notification'] if (
        'Telegram' in configurations) else False 

    if (notification):

        _telegram = configurations['Telegram']

        telegram = Telegram(
            chat_code=_telegram['Chat ID'],
            token=_telegram['Token']
        )
    else: 
        telegram = None 

    _open_sea =  configurations['Open Sea'] if (
        'Open Sea' in configurations
    ) else None 
    
    open_sea = OpenSea(
        api_key=_open_sea['Api Key'],
        collection_slug=_open_sea['Collection Slug'],
        asset_contract_address=_open_sea['Asset Contract Address'],
        test=_open_sea['Test'],
        telegram=telegram
    ) if (_open_sea != None) else exit('I need Open Sea configurations.')
