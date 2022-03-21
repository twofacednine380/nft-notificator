from src.collections.crypto_punks.crypto_punks_attributes import (
    Hair,
    Eyes,
    FacialHair,
    NeckAccessory,
    MouthProp,
    Mouth,
    Blemishes,
    Ears,
    Nose
)

class Attributes:

    def __init__(self) -> None:
        
        self.hair = Hair() 
        self.eyes = Eyes()
        self.facial_hair = FacialHair()
        self.neck_accessory = NeckAccessory()
        self.mouth_prop = MouthProp()
        self.mouth = Mouth()
        self.blemishes = Blemishes()
        self.ears = Ears()
        self.nose = Nose()

        self.attributes = [
            self.hair,
            self.eyes,
            self.facial_hair,
            self.neck_accessory,
            self.mouth_prop,
            self.mouth,
            self.blemishes,
            self.ears,
            self.nose
        ]