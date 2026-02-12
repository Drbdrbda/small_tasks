a = int(input())
b = int(input())

flag = 0
num = 0

for i in range(a, b + 1):
    flag = 0
    for j in range(1, i):
        if i % j == 0 and j != 1:
            flag = 1
    if flag == 0 and i != 1:
        num = i
        print(num)