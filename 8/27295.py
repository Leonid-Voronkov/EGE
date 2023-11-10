import itertools
listString = itertools.permutations('СВЕТА', 5)
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('ЕА') == 0 and line.count('АЕ') == 0:
        count += 1
print(count)