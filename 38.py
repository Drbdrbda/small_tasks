grade = int(input())
counter = 0

while grade > 0 and grade <= 5:
    if grade == 5:
        counter += 1
    grade = int(input())
    
print(counter)