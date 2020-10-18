EARTH_GRAVITY = 9.81373 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.622 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 331.8 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

import math

def volny_pad_zem(vyska):
    '''
    Výpočet rychlosti volného pádu na Zemi v m/s
    '''
    return EARTH_GRAVITY * (math.sqrt((2 * vyska) / EARTH_GRAVITY))

def volny_pad_mesic(vyska):
    '''
    Výpočet rychlosti volného pádu na Měsíci v m/s
    '''
    return MOON_GRAVITY * (math.sqrt((2 * vyska) / MOON_GRAVITY))

def index_lomu(rychlost):
    '''
    Index lomu světla při zadané rychlosti
    '''
    return SPEED_OF_LIGHT / rychlost

def rychlost_zvuku_pri_teplote(teplota):
    '''
    Rychlost zvuku ve vzduchu při dané teplotě v m/s
    '''
    return SPEED_OF_SOUND + 0.61 * teplota