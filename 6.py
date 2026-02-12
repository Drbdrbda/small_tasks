x = int(input())

for i in range(1000):
    if x == i and i < 14:
        print('детство')
    elif x == i and i < 25:
        print('молодость')
    elif x == i and i < 60:
        print('зрелость')
    elif x == i and i >= 60:
        print('старость')