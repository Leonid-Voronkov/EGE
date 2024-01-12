for num in range(100, 200):
    r = bin(num)[2:]
    a = num % 3
    b = bin(a)[2:].zfill(2)
    r += b
    c = int(r, 2)
    d = c % 5
    e = bin(d)[2:].zfill(3)
    r += e
    R = int(r, 2)
    z = R // num
    print(num, "->", R, '->', z)





