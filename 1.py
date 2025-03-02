digits = str(input())

print('\n')
for i in range(len(digits)):
    print(digits[i], digits[(i+1)%3], digits[(i+2)%3], sep='')
    print(digits[i], digits[(i+2)%3], digits[(i+1)%3], sep='')
