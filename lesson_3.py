a = input()
i = 0
if   (int(a[(i+1)%3]) - int(a[i%3])) + int(a[(i+1)%3]) == int(a[(i+2)%3]):
    print('YES')
else:
    print('NO')