'''
 Set je množina jedinečných hodnot
 A set is a collection which is unordered and unindexed.
 In Python sets are written with curly brackets.
'''
# Set je množina, která je neseřazená a neindexovaná
# V Pythonu je set (množiny) zapisovány pomocí složených závorek
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Once a set is created, you cannot change its items, but you can add new items. 
# To add one item to a set use the add() method.
# Pokud je set (množina) jednou vytvořena, nemůžeme změnit její položky, ale můžeme přidat nové položky
# Pro přidání jedné nové položky do množiny použíjeme metodu add()
set_chars.add('V')

# To add more than one item to a set use the update() method.
# Pro přidání více než jedné položky do množiny, použijeme metodu update()
set_chars.update('X', 'Y', 'Z')

# To remove an item in a set, use the remove(), or the discard() method.
# Pro odstranění položky z množiny použijeme metodu remove() nebo discard()
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# The clear() method empties the set
# Metoda clear() vyprázdní celý set
set_chars.clear()

# The del keyword will delete the set completely:
# Zkratka del kompletně smaže set
del set_chars

# Přístup k hodnotám množiny
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# my_set[1]
# Nemůžeme přistoupit k položce (hodnotě), pomocí indexu, jelikož je set neseřazený a neidexovaný

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Ale můžeme projít set pomocí cyklu for, nebo se "zeptat" jestli je specifická hodnota přítomna v setu, použitím in
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
