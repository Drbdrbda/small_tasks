num = input()

ost = 0
for i in num:
    if i == '.':
        ost = 1
    elif ost == 1:
        ost = 0
        print(i)


'''
num = float(input())
print(int((10 * num)%10))

print(ost)
'''
