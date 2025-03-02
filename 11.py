num1 = int(input())
num2 = int(input())

sign = input()

true_sign = {'+', '-', '*', '/'}

if sign in true_sign:
    if sign == '+':
        print(num1 + num2)
    elif sign == '-':
        print(num1 - num2)
    elif sign == '*':
        print(num1 * num2)
    elif sign == '/' and num2 != 0:
        print(num1/num2)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')