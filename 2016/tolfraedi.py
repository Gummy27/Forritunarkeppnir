from collections import defaultdict

employees = defaultdict(lambda : 0)

for x in range(int(input())):
    action, age = input().split(" ")

    if(action == "A"):
        employees[age] += 1
    else:
        employees[age] -= 1
    
    minAge, sumAge, maxAge, teljari = 0, 0, 0, 0
    for age, counter in employees.items():
        age = int(age)

        if(counter):
            if(not minAge):
                minAge = age
                
            minAge = min([minAge, age])
            maxAge = max([maxAge, age])

        sumAge += age*counter
        teljari += counter

    print(employees)
    if(sumAge):
        print(minAge, maxAge, sumAge / teljari)
    else:
        print(-1, -1, -1)




'''
employees = []
for x in range(int(input())):
    action, age = input().split(" ")
    if(action == "A"):
        employees.append(int(age))
    else:
        employees.remove(int(age))
    
    if(len(employees)):
        print(min(employees), max(employees), sum(employees)/len(employees))
    else:
        print(-1, -1, -1)
'''

