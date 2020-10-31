def charFrequency(input):
    char = []
    for i in input:
        if not (i, input.count(i)) in char:
            char.append((i, input.count(i)))
    return sorted(char, key=lambda item: item[1], reverse=True)

input = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
print(f'Věta: {input}\nČetnost výskytu písmen:\n-----------------------')
print(charFrequency(input))