n = int(input())

sum_nums = 0
for i in range(1, n+1):
    if n % i == 0:
        sum_nums += i
print(sum_nums)
