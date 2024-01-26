from itertools import product

# Из числа в строку (Найти слово под определённым номером)
print(list(product('ЛРНТ', repeat=5))[149])

# Из строки в число (Найти позицию некоторого слова)
pos = 0
for line in product('АОУ', repeat=5):
    if ''.join(line) == 'УАУАУ':
        print(pos + 1)
        break
    pos += 1
