num = int(input())

c = num%10
b = (num%100)//10
a = (num%1000)//100

if max(a,b,c) - min(a,b,c) == (a + b + c) - max(a,b,c) - min(a,b,c):
    print('Число интересное')
else:
    print('Число неинтересное')