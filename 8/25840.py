import itertools
listString = itertools.product('БЕЛКА', repeat=4)
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('Б') == 1:
        count += 1
print(count)