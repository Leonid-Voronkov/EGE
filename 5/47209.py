for num in range(1, 100):
    r = bin(num)[2:]
    if r.count("1") % 2 == 0:
        r = "10" + r[2:] + "0"
    else:
        r = "11" + r[2:] + "1"
    R = int(r, 2)
    if R > 40:
        print(num)
        break


