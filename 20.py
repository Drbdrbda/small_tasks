from math import *

a = float(input())
b = float(input())
c = float(input())

#x = 0
#a*x**2 + b*x + c == 0

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b - sqrt(D)) / (2*a)
    x2 = (-b + sqrt(D)) / (2*a)
    if x1 < x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
if D == 0:
    x = -1*(b / (2*a)) 
    print(x)
if D < 0:
    print('Нет корней')