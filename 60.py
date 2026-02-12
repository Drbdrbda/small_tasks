n = int(input())
total = 0
s = ''
for i in range(n):
    s = input()
    counter = s.count('11')
    if counter >= 3:
        total += 1
print(total)