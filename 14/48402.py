nums = []
for x in '0123456789AB':
        res = int(f'3{x}DA', 14) + int(f'5{x}A6', 12)
        if res % 81 == 0:
            nums.append(res)
print(min(nums) // 81)
