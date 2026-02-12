n = input()

flag = 'YES'
i = 0
for i in range(0, len(n) - 1):
    if int(n[i]) < int(n[i+1]):
        flag = 'NO'

print(flag)