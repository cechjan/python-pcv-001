'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# Sbírka, která je neseřazená, měnitelná a indexovaná.
# V Pythonu jsou dictionaries (slovníky) zapisovány pomocí složených závorek a mají klíč a hodnotu.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
slunecni_soustava = {
  'mars' : {
    # Orbitální rychlost - maximální, průměrná, minimální (v km/s)
    'orbit_rychlost' : [26.499, 24.077, 21.972],
    # Pořadí od Slunce
    'poradi' : 4,
    # (v km/s)
    'rychlost_rotace' : 868.22,
    # Povrchová teplota - maximální, průměrná, minimální (ve °C)
    'povrchova_teplota' : [35, -63, -143],
    'vetsi_nez_zeme' : False,
    'mesice' : {'Phobos', 'Deimos'}
  },
  'neptun' : {
    'orbit_rychlost' : [5.479, 5.432, 5.385],
    'poradi' : 8,
    'rychlost_rotace' : 9660,
    'povrchova_teplota' : ['?', -220.15, -223.15],
    'vetsi_nez_zeme' : True,
    'mesice' : {'Triton', 'Thalassa', 'Naiad', 'Nereida', 'Proteus', 'Neso', 'Despina', 'S/2004 N 1', 'Galatea', 'Halimede', 'Psamathe', 'Laomedeia', 'Larissa', 'Sao'}
  },
  'merkur' : {
    'orbit_rychlost' : [58.98, 47.36, 38.86],
    'poradi' : 1,
    'rychlost_rotace' : 10.892,
    'povrchova_teplota' : [426, 167, -183],
    'vetsi_nez_zeme' : False,
    'mesice': {},
  }
}

# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
slunecni_soustava['venuse'] = {'orbit_rychlost' : [35.259, 35.020, 34.784], 'poradi' : 2, 'rychlost_rotace' : 6.52, 'povrchova_teplota' : [500, 464, -45], 'vetsi_nez_zeme' : False, 'mesice' : {}}
slunecni_soustava.pop('mars')
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
line = 200
print(f'\nSlovník slunecni_soustava\n{"-" * line}')
print('planeta', end="         ")
print('               '.join(slunecni_soustava[next(iter(slunecni_soustava))].keys()))
print(f'{"-" * line}')
for id, info in slunecni_soustava.items():
  print(f'{id.ljust(15)}', end=" ")
  for key in info:
    print(str(info[key]).ljust(29), end="")
  print("\n")
print(f'{"-" * line}\nPočet záznamů: {len(slunecni_soustava.keys())}')

'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''