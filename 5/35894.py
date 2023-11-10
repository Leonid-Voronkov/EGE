for num in range(105, 500):
    r = bin(num)[2:]
    c = 1
    while c <= 3:
        a = r.count("1")
        b = r.count("0")
        if a == b:
            r += r[-1]
        if a < b:
            r += "1"
        if a > b:
            r += "0"
        c += 1
    R = int(r, 2)
    if R % 4 == 0:
        print(num)
        break


