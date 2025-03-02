cities = []

for i in range(0,3):
    cities.append(input())
print(cities)

i = 0
min_len = len(cities[i])
max_len = len(cities[i+1])
print(min_len, max_len)
min_name = ''
max_name = ''

for i in range(0,3):
    if min_len >= len(cities[i]):
        print(len(cities[i]))
        min_name = cities[i]
        print(min_name)
    if max_len <= len(cities[i]):
        print(len(cities[i]))
        max_name = cities[i]
        print(min_name)

print(min_name)
print(max_name)