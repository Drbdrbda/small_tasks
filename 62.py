n = int(input())

x = 0

while n:
    x += n % 10
    n = n // 10
    if n == 0:
        n = x
        if x // 10 == 0 and x != 0:
            break
        x = 0
print(n)
