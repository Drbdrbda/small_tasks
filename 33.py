n = int(input())
x = 0
y = 0
z = 1

for _ in range(0, n):
    x = y + z
    z = y
    y = x
    print(y, end=' ')