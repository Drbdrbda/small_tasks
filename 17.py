cities = []
cities_len = []

for i in range(0,3):
    cities.append(input())
for j in range(0,3):
    cities_len.append(len(cities[j]))

print(cities)
print(cities_len)

i = 0
min_len = cities_len[i]
max_len = cities_len[i]
print(min_len, max_len)

for i in range(0,3):
    if min_len >= cities_len[i]:
        min_len = cities_len[i]
    if max_len <= cities_len[i]:
        max_len = cities_len[i]

print(min_len)
print(max_len)

#a = input()
#b = input()
#c = input()
