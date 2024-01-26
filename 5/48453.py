for i in range(0, 1000):
    s = bin(i)[2:]
    s.replace('1', 'a', 1)
    s.replace('0', '1', 1)
    s.replace('a', '0', 1)
    s = int(s, 2)
    res = i - s
    if res == 979:
        print(res)
