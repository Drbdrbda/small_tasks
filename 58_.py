s = input()
a = 0
b = 0

for i in range(len(s)):
    if s[i] in 'ауоыиэяюе':
        a += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщ' and :
        print(s[i])
        b += 1
        
print(f'Количество гласных букв равно {a}')
print(f'Количество согласных букв равно {b}'