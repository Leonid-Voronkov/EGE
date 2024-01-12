m = 0
max_i = 0
def A(i):
    s = '1' * i
    while '1111' in s:
            s = s.replace('1111', '22', 1)
            s = s.replace('222', '1', 1)
    return s

for i in range(201, 1000):
    count = A(i).count('1')
    if count > m:
        m = count
        max_i = i
print(max_i)
