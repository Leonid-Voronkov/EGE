n = 3 * 343 ** 8 + 5 * 49 ** 12 + 7 ** 15 - 49
s = ''
while n != 0:
    s += str(n % 7)
    n = n // 7
print(s)