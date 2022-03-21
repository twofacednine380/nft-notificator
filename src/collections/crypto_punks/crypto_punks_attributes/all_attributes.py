from src.collections import Trait

class Hair:

    name_type = "Hair"

    beanie = Trait('Beanie', 227.27)
    pilot_helmet = Trait('Pilot Helmet', 185.19)
    tiara = Trait("Tiara", 181.82)
    orange_side = Trait("Orange side", 147.06)
    pig_tails = Trait("Pigtails", 106.38)
    pink_with_hat = Trait("Pink With Hat", 105.26)
    top_hat = Trait("Top Hat", 86.96)
    blonde_short = Trait("Blonde Short", 77.52)
    wild_white_hair = Trait("Wild White Hair", 73.53)
    cowboy_hat = Trait("Cowboy Hat", 70.42)
    straight_hair_blonde = Trait("Straight Hair Blonde", 69.44)
    wild_blonde = Trait("Wild Blonde", 69.44)
    blonde_bob = Trait("Blonde Bob", 68.03)
    half_shaved = Trait("Half Shaved", 68.03)
    red_mohawk = Trait("Red Mohawk", 68.03)
    vampire_hair = Trait("Vampire Hair", 68.03)
    clown_hair_green = Trait("Clown Hair Green", 67.57)
    straight_hair_dark = Trait("Straight Hair Dark", 67.57)
    straight_hair = Trait("Straight Hair", 66.23)
    dark_hair = Trait("Dark Hair", 66.69)
    purple_hair = Trait("Purple Hair", 60.61)
    tassle_hat = Trait("Tassle Hat", 56.18)
    fedora = Trait("Fedora", 53.76)
    police_cap = Trait("Police Cap", 49.26)
    none = Trait(None, 40.65)
    cap_forward = Trait("Cap Forward", 39.37)
    hoodie = Trait("Hoodie", 38.61)
    do_rag = Trait("Do-rag", 33.33)
    shaved_head = Trait("Shaved Head", 33.33)
    peak_spike = Trait("Peak_Spike", 33.00)
    cap = Trait("Cap", 28.49)
    headband = Trait("Headband", 24.63)
    crazy_hair = Trait("Crazy Hair", 24.15)
    knitted_cap = Trait("Knitted Cap", 23.87)
    mohawk_dark = Trait("Mohawk Dark", 23.31)
    mohawk = Trait("Mohawk", 22.68)
    mohawk_thin = Trait("Mohawk Thin", 22.68)
    frumpy_hair = Trait("Frumpy Hair", 22.62)
    wild_hair = Trait("Wild Hair", 22.37)
    messy_hair = Trait("Messy Hair", 21.74)
    stringy_hair = Trait("Stringy Hair", 21.60)
    bandana = Trait("Bandana", 20.79)

    objects = [
        beanie,
        pilot_helmet,
        tiara,
        orange_side,
        pig_tails,
        pink_with_hat,
        top_hat,
        blonde_short,
        wild_white_hair,
        cowboy_hat,
        straight_hair_blonde,
        wild_blonde,
        blonde_bob,
        half_shaved,
        red_mohawk,
        vampire_hair,
        clown_hair_green,
        straight_hair_dark,
        straight_hair,
        dark_hair,
        purple_hair,
        tassle_hat,
        fedora,
        police_cap,
        none,
        cap_forward,
        hoodie,
        do_rag,
        shaved_head,
        peak_spike,
        cap,
        headband,
        crazy_hair,
        knitted_cap,
        mohawk_dark,
        mohawk,
        mohawk_thin,
        frumpy_hair,
        wild_hair,
        messy_hair,
        stringy_hair,
        bandana,
    ]

class Eyes:

    name_type = "Eyes"

    welding_goggles = Trait("Welding Goggles", 116.28)
    purple_eye_shadow = Trait("Purple Eye Shadow", 38.17)
    blue_eye_shadow = Trait("Blue Eye Shadow", 38.17)
    green_eye_shadow = Trait("Green Eye Shadow", 36.90)
    threed_glasses = Trait("3D Glasses", 34.97)
    eye_mask = Trait("Eye Mask", 34.13)
    vr = Trait("VR", 30.12)
    small_shades = Trait("Small Shades", 26.46)
    clown_eyes_green = Trait("Clown Eyes Green", 26.18)
    clown_eyes_blue = Trait("Clown Eyes Blue", 26.04)
    eye_patch = Trait("Eyes Patch", 21.69)
    classic_shades = Trait("Classic Shades", 19.92)
    regular_shades = Trait("Regular Shades", 18.98)
    big_shades = Trait("Big Shades", 18.69)
    horned_rim_glasses = Trait("Horned Rim Glasses", 18.69)
    nerd_glasses = Trait("Nerd Glasses", 17.48)
    none = Trait(None, 2.55)

    objects = [
        welding_goggles,
        purple_eye_shadow,
        blue_eye_shadow,
        green_eye_shadow,
        threed_glasses,
        eye_mask,
        vr,
        small_shades,
        clown_eyes_green,
        clown_eyes_blue,
        eye_patch,
        classic_shades,
        regular_shades,
        big_shades,
        horned_rim_glasses,
        nerd_glasses,
        none
    ]

class FacialHair:

    name_type = "Facial Hair"

    bid_beard = Trait("Big Beard", 68.49)
    front_beard_dark = Trait("Front Beard Dark", 38.46)
    handlebars = Trait("Handlebars", 38.02)
    front_beard = Trait("Front Beard", 36.63)
    chinstrap = Trait("Chinstrap", 35.46)
    luxurious_beard = Trait("Luxurious Beard", 34.97)
    mustache = Trait("Mustache", 34.72)
    normal_beard_black = Trait("Normal Beard Black", 34.60)
    normal_beard = Trait("Normal Beard", 34.25)
    goat = Trait("Goat", 33.90)
    muttonchops = Trait("Muttonchops", 33)
    shadow_beard = Trait("Shadow Beard", 19.01)
    none = Trait(None, 1.54)

    objects = [
        bid_beard,
        front_beard_dark,
        handlebars,
        front_beard,
        chinstrap,
        luxurious_beard,
        mustache,
        normal_beard_black,
        normal_beard,
        goat,
        muttonchops,
        shadow_beard,
        none
    ]


class NeckAccessory:

    name_type = "Neck Accessory"

    choker = Trait("Choker", 208.33)
    silver_chain = Trait("Silver Chain", 64.10)
    gold_chain = Trait("Gold Chain", 59.17)
    none = Trait(None, 1.05)

    objects = [
        choker, 
        silver_chain,
        gold_chain,
        none
    ]

class MouthProp:
    
    name_type = "Mouth Prop"

    medical_mask = Trait("Medical Mask", 57.14)
    vape = Trait("Vape", 36.76)
    pipe = Trait("Pipe", 31.55)
    cigarette = Trait("Cigarette", 10.41)
    none = Trait(None, 1.21)

    objects = [ 
        medical_mask,
        vape,
        pipe,
        cigarette,
        none 
    ]

class Mouth:

    name_type = "Mouth"

    buck_teeth = Trait("Buck Teeth", 128.21)
    smile = Trait("Smile", 42.02)
    frown = Trait("Frown", 38.31)
    black_lipstick = Trait("Black Lipstick", 16.21)
    purple_lipstick = Trait("Purple Lipstick", 15.27)
    hot_lipstick = Trait("Hot Lipstick", 14.37)
    none = Trait(None, 1.34)

    objects = [
        buck_teeth,
        smile,
        frown,
        black_lipstick,
        purple_lipstick,
        hot_lipstick,
        none 
    ]

class Blemishes: 

    name_type = "Blemishes"

    spots = Trait("Spots", 80.65)
    rosy_cheeks = Trait("Rosy Cheeks", 78.13)
    mole = Trait("Mole", 15.53)
    none = Trait(None, 1.10)

    objects = [
        spots,
        rosy_cheeks,
        mole,
        none
    ]

class Ears:

    name_type = "Ears"

    earring = Trait("Earring", 4.07)
    none = Trait(None, 1.33)

    objects = [
        earring,
        none
    ]

class Nose:

    name_type = "Nose"

    clown_nose = Trait("Clown Nose", 47.17)
    none = Trait(None, 1.02)

    objects = [
        clown_nose, 
        none
    ]
