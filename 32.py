x = 0
nums = 0
for _ in range(0,10):
    x = int(input())
    if x % 2 == 0:
        nums +=1

if nums == 10:
    print('YES')
else:
    print('NO')


