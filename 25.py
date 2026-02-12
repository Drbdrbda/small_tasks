from math import log

n = int(input())

f = 0
for i in range(1,n+1):
    f += 1/i
print(f - log(n))
