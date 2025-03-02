
num = int(input())

if not (0 <= num <= 36):
    print('ошибка ввода')
elif num == 0:
    print('зеленый')
elif num % 2 == 0 and num > 0:
    if 11 < num <= 18 or 29 < num <= 36:
        print('красный')
    else: 
        print('черный')
elif num > 0:
    if 1 <= num < 10 or 19 <= num < 28:
        print('красный')
    else: 
        print('черный')