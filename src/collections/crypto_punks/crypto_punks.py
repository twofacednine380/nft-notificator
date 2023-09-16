from src.collections.crypto_punks import General, Attributes

class CryptoPunks:

    collection_slug = 'crypto-punks'
    asset_contract_address = '0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb'
    name = 'CryptoPunks'

    def __init__(self) -> None:
        
        self.general = General()
        self.attributes = Attributes()

        