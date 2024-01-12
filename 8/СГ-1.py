import itertools
listString = itertools.product('АВЕСТ', repeat=5)
count = 0
for str in listString:
    line = ''.join(str)
    if line == 'СВЕТА':
        break
    count += 1
print(count)
print(int('31240', 5) + 1)
