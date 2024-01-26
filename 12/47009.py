for a in range(20):
    for b in range(20):
        for c in range(20):
            s = '0' + a * '1' + b * '2' + c * '3' + '0'
            while '00' not in s:
                s = s.replace("01", "210", 1)
                s = s.replace("02", "3101", 1)
                s = s.replace("03", "2012", 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(a + b + c + 2)





