import itertools
listString = itertools.permutations('СВЕТЛАНА',8)
a = set()
for str in listString:
    line = ''.join(str)
    if line.count('АА') == 0 :
        a.add(line)
print(len(a))