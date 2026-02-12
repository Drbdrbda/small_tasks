digits = str(input())

print('\n')
for i in range(len(digits)):
    print(digits[i], digits[(i+1)%3], digits[(i+2)%3], sep='')
    print(digits[i], digits[(i+2)%3], digits[(i+1)%3], sep='')

'''
num = int(input())

a = num % 10
b = (num // 10) % 10
c = num // 100

digits = [a, b, c]
print('\n')
for i in range(len(digits)):
    print(digits[i], digits[(i+1)%3], digits[(i+2)%3], sep='')
    print(digits[i], digits[(i+2)%3], digits[(i+1)%3], sep='')

i=0
print(digits[i], digits[i+1], digits[i+2], sep='')
print(digits[i], digits[i+2], digits[i+1], sep='')
i+=1
print(digits[i], digits[i+1], digits[(i+2)%3], sep='')
print(digits[i], digits[(i+2)%3], digits[i+1], sep='')
i+=1
print(digits[i], digits[(i+1)%3], digits[(i+2)%3], sep='')
print(digits[i], digits[(i+2)%3], digits[(i+1)%3], sep='')

print(digits[i], digits[i+1], digits[i-1], sep='')
print(digits[i], digits[i-1], digits[i+1], sep='')

i+=1
print(digits[i], digits[i-1], digits[i-2], sep='')
print(digits[i], digits[i-2], digits[i-1], sep='')
'''