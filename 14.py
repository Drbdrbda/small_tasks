nums = []

for i in range(3):
    nums.append(int(input()))

for i in range(0, len(nums)-1):
    for j in range(0, (len(nums)-1) -i):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1] , nums[j]

for num in nums:
    print(num, sep='\n')
