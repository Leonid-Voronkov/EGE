import itertools
listString = itertools.product('АНДРЕЙ', repeat=7)
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('Й') == 1 and line.count('А') == 1 and line[0] != 'Й':
        count += 1
print(count)