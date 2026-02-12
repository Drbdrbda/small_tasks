num = int(input())

while num:
    last_digit = num % 10
    num = num // 10
    print(last_digit, end='')



'''
num = input()
reversed_num = ''
for i in range(len(num) -1, -1, -1):
    reversed_num += num[i]

print(reversed_num)
'''