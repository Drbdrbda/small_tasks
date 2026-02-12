stop = {'стоп', 'хватит', 'достаточно'}
word = input()
counter = 0

while word not in stop:
    counter += 1
    word = input()

print(counter)