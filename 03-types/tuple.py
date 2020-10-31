'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
In Python tuples are written with round brackets.
'''
# V Pythonu tuples (n-tice) jsou zapisovány pomocí kulatých závorek

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
# Pro vytovoření tuple pouze s jednou položkou, musíme přidat čárku po položce, jinak Python nepozná, že se jedná o tuple
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# Při výpisu můžeme specifikovat rozsah indexů pomocí startovního indexu a končícího indexu
# Při specifikování rozsahu bude vrácená hodnota nový tuple se specifikovanými položky
print(f'chars[2:5]: {chars[2:5]}')

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Specify negative indexes if you want to start the search from the end of the tuple: 
# This example returns the items from index -4 (included) to index -1 (excluded)
# Záporný index znamená začátek od konce, -1 "ukazuje" na poslední položku, -2 na předposlední atd.
# Používejte záporné indexy pokud chcete začít hledání od konce tuple
# Tento příklad vrací položku z indexu -4 (včetně) do indexu -1 (bez)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# To determine how many items a tuple has, use the len() method:
# Pro zjištění kolik položek tuple má, použijeme metodu le()
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
