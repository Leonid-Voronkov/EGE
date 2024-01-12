print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = ((x == y) and (w <= z))
                F2 = ((x <= y) <= (w == z))
                if F1 == 1 and w == 1 and x == 0:
                    print(x, y, z, w)




