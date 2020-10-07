import math

print('Výpočet čisté mzdy')
#jmeno = str(input('Zadejte svoje křestní jméno: '))
jmeno = input('Zadejte svoje křestní jméno: ')
while jmeno.isnumeric() or jmeno[0] == '-':
    jmeno = input('Zadejte svoje křestní jméno: ')
prijmeni = input('Zadejte svoje příjmení: ')
while prijmeni.isnumeric() or prijmeni[0] == '-':
    prijmeni = input('Zadejte svoje příjmení: ')

pohlavi = input('Muž / Žena: ').lower()
while not(pohlavi == 'muž' or pohlavi == 'žena' or pohlavi == 'muz' or pohlavi == 'zena'):
    pohlavi = input('Muž / Žena: ')

# HM = int(input('Zadejte výši svojí hrubé mzdy v Kč: '))
HM = input('Zadejte výši svojí hrubé mzdy v Kč: ')
while not (HM.isdigit() and int(HM) > 0):
    HM = input('Zadejte výši svojí hrubé mzdy v Kč: ')
HM = int(HM)
# while HM < 0:
#     HM = int(input('Zadejte výši svojí hrubé mzdy v Kč: '))

sleva_na_poplatnika = input('Uplatňujete slevu na poplatníka? (ano / ne): ').lower()
while not(sleva_na_poplatnika == 'ano' or sleva_na_poplatnika == 'ne'):
    sleva_na_poplatnika = input('Uplatňujete slevu na poplatníka? (ano / ne): ').lower()

#sleva_na_deti = int(input('Zadejte počet dětí, na které používáte daňové zvýhodnění. (0 / 1 / ...): '))
sleva_na_deti = input('Zadejte počet dětí, na které používáte daňové zvýhodnění. (0 / 1 / ...): ')
#while sleva_na_deti < 0:
while not (sleva_na_deti.isdigit() and int(sleva_na_deti) >= 0):
    sleva_na_deti = input('Zadejte počet dětí, na které používáte daňové zvýhodnění. (0 / 1 / ...): ')
sleva_na_deti = int(sleva_na_deti)

dalsi_slevy = input('Uplatňujete další slevy na dani? (ano / ne): ').lower()
while not(dalsi_slevy == 'ano' or dalsi_slevy == 'ne'):
    dalsi_slevy = input('Uplatňujete další slevy na dani? (ano / ne): ').lower()

if dalsi_slevy == 'ano':
    castecny_invalidni_duchod = input('Uplatňujete slevu na částečný invalidní důchod? (ano / ne): ').lower()
    while not (castecny_invalidni_duchod == 'ano' or castecny_invalidni_duchod ==  'ne'):
        castecny_invalidni_duchod = input('Uplatňujete slevu na částečný invalidní důchod? (ano / ne): ').lower()

    if castecny_invalidni_duchod == 'ne':
        plny_invalidni_duchod = input('Uplatňujete slevu na plný invalidní důchod? (ano / ne): ').lower()
        while not (plny_invalidni_duchod == 'ano' or plny_invalidni_duchod == 'ne'):
            plny_invalidni_duchod = input('Uplatňujete slevu na plný invalidní důchod? (ano / ne): ').lower()

    sleva_na_studenta = input('Uplatňujete slevu na studenta? (ano / ne): ').lower()
    while not (sleva_na_studenta == 'ano' or sleva_na_studenta == 'ne'):
        sleva_na_studenta = input('Uplatňujete slevu na studenta? (ano / ne): ').lower()


#srazky = int(input('Napište částku, kterou si necháváte měsíčně srážet např. penzijní pojištění. V Kč: '))
srazky = input('Napište částku, kterou si necháváte měsíčně srážet např. penzijní pojištění. V Kč: ')
#while srazky < 0:
while not (srazky.isdigit() and int(srazky) >= 0):
    srazky = input('Napište částku, kterou si necháváte měsíčně srážet např. penzijní pojištění. V Kč: ')
srazky = int(srazky)


# Výpis
sleva_na_poplatnika_castka = 2070
sleva_na_deti_castka_1 = 1267
sleva_na_deti_castka_2 = 1617
sleva_na_deti_castka_3 = 2017
castecny_invalidni_duchod_castka = 210
plny_invalidni_duchod_castka = 420
sleva_na_studenta_castka = 335
socialni_pojisteni_zamestnance = 0.065      # 6.5%
zdravotni_pojisteni_zamestnance = 0.045      # 4.5%
oddelovac = '---------------------------------------------'

if pohlavi == 'muž' or pohlavi == 'muz':
    print('\nPan {} {}'.format(jmeno, prijmeni))
else:
    print('\nPaní {} {}'.format(jmeno, prijmeni))

print(oddelovac)

print('Hrubá mzda: {}'.format(HM))

print(oddelovac)

SHM = HM * 1.34
SHM = int(math.ceil(SHM / 100)) * 100
print('Zaokrouhlená Superhrubá mzda: {}'.format(SHM))

print(oddelovac)

ZDP = int(SHM * 0.15)
print('Záloha na daň z příjmu: {}'.format(ZDP))

print(oddelovac)

if sleva_na_poplatnika == 'ano':
    ZDP -= sleva_na_poplatnika_castka
    print('Sleva na poplatníka: {}'.format(sleva_na_poplatnika_castka))
    print(oddelovac)
if dalsi_slevy == 'ano':
    if castecny_invalidni_duchod == 'ano':
        ZDP -= castecny_invalidni_duchod_castka
        print('Sleva na částečný invalidní důchod: {}'.format(castecny_invalidni_duchod_castka))
        print(oddelovac)
    elif plny_invalidni_duchod == 'ano':
        ZDP -= plny_invalidni_duchod_castka
        print('Sleva na plný invalidní důchod: {}'.format(plny_invalidni_duchod_castka))
        print(oddelovac)
    if sleva_na_studenta == 'ano':
        ZDP -= sleva_na_studenta_castka
        print('Sleva na studenta: {}'.format(sleva_na_studenta_castka))
        print(oddelovac)

if sleva_na_deti > 0:
    if sleva_na_deti == 1:
        ZDP -= sleva_na_deti_castka_1
        print('Sleva na děti: {}'.format(sleva_na_deti_castka_1))
        print(oddelovac)
    elif sleva_na_deti == 2:
        ZDP -= (sleva_na_deti_castka_1 + sleva_na_deti_castka_2)
        print('Sleva na děti: {}'.format(sleva_na_deti_castka_1 + sleva_na_deti_castka_2))
        print(oddelovac)
    elif sleva_na_deti == 3:
        ZDP -= (sleva_na_deti_castka_1 + sleva_na_deti_castka_2 + sleva_na_deti_castka_3)
        print('Sleva na děti: {}'.format(sleva_na_deti_castka_1 + sleva_na_deti_castka_2 + sleva_na_deti_castka_3))
        print(oddelovac)
    else:
        nad_3 = sleva_na_deti - 3
        nad_3 *= sleva_na_deti_castka_3
        ZDP -= (sleva_na_deti_castka_1 + sleva_na_deti_castka_2 + sleva_na_deti_castka_3 + nad_3)
        print('Sleva na děti: {}'.format(sleva_na_deti_castka_1 + sleva_na_deti_castka_2 + sleva_na_deti_castka_3 + nad_3))
        print(oddelovac)


dan_po_slevach = ZDP
print('Daň po slevách: {}'.format(dan_po_slevach))

print(oddelovac)

if dan_po_slevach < 0:
    print('Daňový bonus: {}'.format(abs(dan_po_slevach)))
    print(oddelovac)

SP = int(HM * socialni_pojisteni_zamestnance)
print('Sociální pojištění zaměstnance (6,5%): {}'.format(SP))

print(oddelovac)

ZP = int(HM * zdravotni_pojisteni_zamestnance)
print('Zdravotní pojištění zaměstnance (4,5%): {}'.format(ZP))

print(oddelovac)

CM = HM - dan_po_slevach - SP - ZP
print('Čistá mzda: {}'.format(CM))

print(oddelovac)

if srazky > 0:
    mzda_k_vyplate = CM - srazky
else:
    mzda_k_vyplate = CM
print('Mzda k výplatě: {}'.format(mzda_k_vyplate))