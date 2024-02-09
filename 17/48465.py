nums = list(map(int, open('48465.txt').readlines()))

min_num = 0
for num in nums:
    if abs(num) % 10 == 6:
        min_num = min(min_num, num)
# Альтернативный (короткий) вариант
# print(min(nums, key=lambda x: x if abs(x) % 10 == 6 else 0))
'''
xor (исключающее ИЛИ)
a b f
0 0 0
0 1 1
1 0 1
1 1 0
В python заменяется на !=
Вместо:
(abs(nums[i]) % 10 == 6 and abs(nums[i + 1]) % 10 != 6) or (abs(nums[i]) % 10 != 6 and abs(nums[i + 1]) % 10 == 6)
Пишем:
((abs(nums[i]) % 10 == 6) != (abs(nums[i + 1]) % 10 == 6))
'''
count = 0
m = 0
for i in range(len(nums) - 1):
    if ((abs(nums[i]) % 10 == 6) != (abs(nums[i + 1]) % 10 == 6)) and (nums[i] ** 2 + nums[i + 1] ** 2 < min_num ** 2):
        count += 1
        m = max(m, nums[i] ** 2 + nums[i + 1] ** 2)
print(count, m)
