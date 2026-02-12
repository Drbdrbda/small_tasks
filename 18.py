str_len = []

for i in range(0,3):
    str_len.append(len(input()))

i = 0
a_min = str_len[i]
a_max = str_len[i]
for i in range(0, len(str_len)):
    if a_min >= str_len[i]:
        a_min = str_len[i]
    if a_max <= str_len[i]:
        a_max = str_len[i]

a_av = sum(str_len) - a_min - a_max

if abs(a_max - a_av) == abs(a_av - a_min):
    print('YES')
else:
    print('NO')


'''
a = len(input())
b = len(input())
c = len(input())

a_min = min(a,b,c)

a_max = max(a,b,c)

a_av = (a + b + c) - a_min - a_max

d1 = abs(a_max - a_av)
d2 = abs(a_av - a_min)

if d1 == d2:
    print('YES')
else:
    print('NO')
'''