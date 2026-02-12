a1 = int(input())
b1 = int(input())

a2 = int(input())
b2 = int(input())

a1 < b1
a2 < b2

if a1 < b2 and a1 > a2 and b1 > b2:
    print(a1, b2)
elif a2 < b1 and a2 > a1 and b2 > b1:
    print(a2, b1)
elif a2 < a1 and b1 < b2:
    print(a1, b1)
elif a1 < a2 and b2 < b1:
    print(a2, b2)
elif a1 == a2 and b1 == b2:
    print(a1, b1)
elif a1 == a2 and b1 > b2:
    print(a1, b2)
elif a1 == a2 and b2 > b1:
    print(a1, b1)
elif b1 == b2 and a1 > a2:
    print(a1, b1)
elif b1 == b2 and a2 > a1:
    print(a2, b1)
elif a1 == b2:
    print(a1)
elif b1 == a2:
    print(b1)
else:
    print('пустое множество')
