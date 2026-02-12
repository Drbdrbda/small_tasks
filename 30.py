n = int(input())

sum_nums = 0

for i in range(1, n + 1):
    sum_nums += ((-1) ** (i+1)) * i
    
print(sum_nums)