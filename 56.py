n = int(input())

for i in range(n):
    for j in range(int(n+1/2)):
        print('*', end='')
    print()

'''
n = int(input())
n = int((n + 1) / 2)

for i in range(1, n + 1):
    print('*' * i)
for j in range(n - 1, -1, -1):
    print('*' * j)'
'''