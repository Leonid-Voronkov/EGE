for num in range(1, 100):
    r = bin(num)[2:]
    r += str(r.count("1") % 2)
    r += str(r.count("1") % 2)
    R = int(r, 2)
    if R < 100:
        print(R)

