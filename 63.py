n = int(input())

sum_fact = 0
x = 1

for i in range(1, n + 1):
    x *= i
    sum_fact += x
print(sum_fact)