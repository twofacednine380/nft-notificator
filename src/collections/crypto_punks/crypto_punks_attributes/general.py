from src.collections.crypto_punks.crypto_punks_attributes import (
    PunkType,
    SkinTone,
    AttributeCount,
    FullType
)

class General:

    def __init__(self) -> None:
        
        self.punk_type = PunkType()
        self.skin_tone = SkinTone()
        self.attribute_count = AttributeCount()
        self.full_type = FullType()

        self.general_attributes = [
            self.punk_type,
            self.skin_tone,
            self.attribute_count,
            self.full_type
        ]