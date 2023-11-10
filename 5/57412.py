b = 0
for num in range(5, 100):
    r = bin(num)[2:]
    if num % 3 == 0:
         r += r[-3:]
    if num % 3 != 0:
        b = 3 * (num % 3)
        r += bin(b)[2:]
    R = int(r, 2)
    if R >= 76:
        print(num)
        break

