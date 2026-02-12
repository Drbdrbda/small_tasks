'''
На вход программе подаётся натуральное число n(n≥2). Затем поступают n целых чисел.
 Напишите программу, которая создаёт из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и так далее).
'''

n = int(input())
digit1 = int(input())
digit2 = 0
sum_digits = 0

sum_list = []

for _ in range(n - 1):
    digit2 = int(input())
    sum_digits = digit1 + digit2
    sum_list.append(sum_digits)
    digit1 = digit2
print(sum_list)