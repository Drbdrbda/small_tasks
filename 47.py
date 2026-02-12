num = int(input())
i = 0
for i in range(2, num + 1):
    if num % i == 0:
        break
print(i)