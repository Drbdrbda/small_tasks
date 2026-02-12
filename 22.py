
m = int(input())
n = int(input())

for i in range(m, n-1, -1):
    if i % 2 == 1:    
        print(i)



m = int(input())
n = int(input())

for i in range(m - 1 + m%2, n-1, -2):

    print(m)


'''

m = int(input())
n = int(input())

for i in range(m, n+1):
    if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
        print(i)




n = int(input())
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')




m = int(input())
n = int(input())

if m > n:
    for i in range(m, n-1, -1):
        print(i)
if m <= n:
    for i in range(m, n+1, 1):
        print(i)



        
x = int(input())

for i in range(0,x+1):
    print(f'Квадрат числа {i} равен {i**2}')




n = int(input())

for i in range(n, 0, -1):
    print('*'*i)




m = int(input())
p = int(input())
n = int(input())

for i in range(1,n+1):
    print(i, m)
    m = m + m*(p/100)
'''
