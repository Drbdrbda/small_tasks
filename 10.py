color1 = input()
color2 = input()

r = str('красный')
b = str('синий')
y = str('желтый')

if (color1 == r or color1 == b or color1 == y) and (color2 == r or color2 == b or color2 == y):
    if color1 == color2:
        print(color1)
    elif color1 == r or color2 == r:
        if color1 == b or color2 == b:
            print('фиолетовый')
        else:
            print('оранжевый')
    else:
        print('зеленый')
else:
    print('ошибка цвета')