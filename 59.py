n = int(input())
x = 0
s = ''

while int(n) != 0 and int(n) > 0:

    x = int(n % 2)
    s += str(x)
    n = n / 2
    
for i in range(len(s) - 1, -1, -1):
    print(s[i], end='')
