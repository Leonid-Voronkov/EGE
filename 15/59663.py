for a in range(64):
    f = True
    for x in range(64):
        for y in range(64):
            if not ((x < a) or (y < a) or (x + 2 * y > 50)):
                f = False
    if f:
        print(a)
        break