n = int(input())

nums = []

for _ in range(0, n):
    nums.append(int(input()))
print(nums)

i, j = 0, 0
max_num = nums[i]
max_num2 = nums[j]

for i in range(len(nums)):
    if  max_num < nums[i]:
        max_num = nums[i]

if max_num == max_num2:
    max_num2 = nums[1]

for j in range(len(nums)):
    if max_num2 < nums[j] and nums[j] != max_num:
        max_num2 = nums[j]

print(max_num)
print(max_num2)

'''
i, j = 0, 0 
for i in range(0, len(nums) - 1):
    for j in range(0, (len(nums) - 1) - i):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
print(nums)
'''