n = int(input())
nn = 0
x = 10
nums = []
for i in range(0,10):
    nn = n * (10 ** i) + nn
    nums.append(nn)

print(nums)
