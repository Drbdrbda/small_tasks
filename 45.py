n = input()

sum_d = 0
quantity = 0
op_d = 1
i = 0
for i in range(0, len(n)):
    sum_d += int(n[i])
    quantity += 1
    op_d *= int(n[i])

print(sum_d)
print(quantity)
print(op_d)
print(sum_d/quantity)
print(n[0]) 
print(int(n[0]) + int(n[quantity -1]))

