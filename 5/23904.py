for num in range(1, 100):
    b = bin(num)[2:]
    if num % 2 == 0:
        b += '00'
    else:
        b += '11'
    r = int(b, 2)
    if r > 134:
        print(num)
        break
