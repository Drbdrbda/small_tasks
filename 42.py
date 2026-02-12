num = input()

i = 0
max_d = int(num[i])
min_d = int(num[i])

for i in range(0, len(num)):
    if max_d <= int(num[i]):
        max_d = int(num[i])
    if int(num[i]) <= min_d:
        min_d = int(num[i])

print(f'Максимальная цифра равна {max_d}')
print(f'Минимальная цифра равна {min_d}')