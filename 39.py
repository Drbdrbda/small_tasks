num = int(input())

counter = 0
i = 0
for i in (25, 10, 5, 1):
    counter += num // i
    num = num % i

print(counter)

'''


a = num // 25
a += num // 10
a += num // 5

print(a)





num = int(input())

counter = 0
if num >= 25:
    counter = num // 25
    num = num % 25
if 25 > num >= 10:
    counter += num // 10
    num = num % 10
if 10 > num >= 5:
    counter += num // 5
    num = num % 5
if 5 > num >= 0:
    counter += num

print(counter)





num = int(input())

moneta = [25, 10, 5, 1]

counter = 0
i = 0
for i in range(0, len(moneta)):
    if num // moneta[i] > 0:
        counter+= num // moneta[i]
        num = num % moneta[i]

print(counter)
'''