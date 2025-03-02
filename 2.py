digit = [int(x) for x in input()]

i = 0
if digit[i] + digit[(i+3)%4] == digit[(i+1)%4] - digit[(i+2)%4]:
    print('ДА')
else:
    print('НЕТ')

