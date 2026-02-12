list_sum_nums = []
sum_nums = 0
counter = 0
for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            for d in range(1, 50):
                if (a ** 3 + b ** 3) == (c ** 3 + d ** 3):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        list_sum_nums.append(c ** 3 + d ** 3)
print(list_sum_nums)



