n = int(input())

nums = 0
max_num = float('-inf')
max_num2 = float('-inf')

for _ in range(0, n):
    nums = int(input())
    if max_num < nums:
        max_num2 = max_num
        max_num = nums
    elif max_num2 < nums and nums != max_num:
        max_num2 = nums


print(max_num)
print(max_num2)
