'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81373 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.622 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 331.8 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

import math

def volny_pad_zem(vyska):
    '''
    Výpočet rychlosti volného pádu na Zemi v m/s
    '''
    return EARTH_GRAVITY * (math.sqrt((2 * vyska) / EARTH_GRAVITY))

print(volny_pad_zem(20))

def volny_pad_mesic(vyska):
    '''
    Výpočet rychlosti volného pádu na Měsíci v m/s
    '''
    return MOON_GRAVITY * (math.sqrt((2 * vyska) / MOON_GRAVITY))

print(volny_pad_mesic(20))

def index_lomu(rychlost):
    '''
    Index lomu světla při zadané rychlosti
    '''
    return SPEED_OF_LIGHT / rychlost

print(index_lomu(2000000))

def rychlost_zvuku_pri_teplote(teplota):
    '''
    Rychlost zvuku ve vzduchu při dané teplotě v m/s
    '''
    return SPEED_OF_SOUND + 0.61 * teplota

print(rychlost_zvuku_pri_teplote(15))