from src.collections import Trait

class PunkType:

    name_type = "Punk Type"
    
    alien = Trait("Alien", 1111.11)
    ape = Trait("Ape", 416.67)
    zombie = Trait("Zombie", 113.64)
    female = Trait("Female", 2.6)
    male = Trait("Male", 1.66)

    objects = [ 
        alien,
        ape,
        zombie,
        female,
        male 
    ]

class SkinTone: 

    name_type = "Skin Tone"

    albino = Trait("Albino", 0)
    dark = Trait("Dark", 0)
    light = Trait("Light", 0)
    mid = Trait("Mid", 0)

    objects = [ 
        albino,
        dark,
        light, 
        mid 
    ]

class AttributeCount:

    name_type = "Attribute Count"

    zero = Trait("0", 1250)
    one = Trait("1", 30.03)
    two = Trait("2", 2.81)
    three = Trait("3", 2.22)
    four = Trait("4", 7.04)
    five = Trait("5", 60.24)
    six = Trait("6", 909.09)
    seven = Trait("7", 10000)

    objects = [
        zero,
        one,
        two,
        three,
        four, 
        five,
        six,
        seven
    ]
    
class FullType:

    name_type = "Full Type"

    female_albino = Trait(
        '{}-{}'.format(
            PunkType.female.value,
            SkinTone.albino.value
        ),
        23.81
    )
    male_albino = Trait(
        '{}-{}'.format(
            PunkType.male.value,
            SkinTone.albino.value
        ),
        16.72
    )
    female_dark = Trait(
        '{}-{}'.format(
            PunkType.female.value,
            SkinTone.dark.value
        ),
        9.08
    )
    male_dark = Trait(
        '{}-{}'.format(
            PunkType.male.value,
            SkinTone.dark.value
        ),
        5.80
    )
    female_light = Trait(
        '{}-{}'.format(
            PunkType.female.value,
            SkinTone.light.value
        ),
        8.73
    )
    male_light = Trait(
        '{}-{}'.format(
            PunkType.male.value,
            SkinTone.light.value
        ),
        5.37
    )
    female_mid = Trait(
        '{}-{}'.format(
            PunkType.female.value,
            SkinTone.mid.value
        ),
        8.52
    )
    male_mid = Trait(
        '{}-{}'.format(
            PunkType.male.value,
            SkinTone.mid.value
        ),
        5.39
    )

    objects = [
        female_albino,
        male_albino,
        female_dark,
        male_dark,
        female_light,
        male_light,
        female_mid,
        male_mid
    ]