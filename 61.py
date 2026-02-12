a = int(input())
b = int(input())

cnt = 0
max_cnt = 0
max_d = 0

for i in range(a, b + 1):
    for j in range(a, b + 1):
        if i % j == 0:
            cnt += j
            if max_cnt < cnt:
                max_cnt = cnt
                max_d = i
                print(max_d, max_cnt, sep ='\n')
            cnt = 0
