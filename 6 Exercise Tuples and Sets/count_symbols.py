text = input()
text_data = {}

for symbol in text:
    if symbol not in text_data:
        text_data[symbol] = 0
    text_data[symbol] += 1
for char, times in sorted(text_data.items()):
    print(f'{char}: {times} time/s')


