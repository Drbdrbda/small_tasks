num = int(input())

max_d = num % 10
min_d = num % 10
n = num % 10

while num:
    if max_d <= n:
        max_d = n
    if n <= min_d:
        min_d = n
    num = num // 10
    n = num % 10

print(f'Максимальная цифра равна {max_d}')
print(f'Минимальная цифра равна {min_d}')