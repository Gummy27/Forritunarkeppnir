from collections import deque

ages = deque([])

sumAge, minAge, maxAge, counter = 0, 0, 0, 0
for x  in range(int(input())):
    action, age = input().split(" ")
    age = int(age)

    if(not counter):
        minAge = age
        maxAge = 0

    if(action == "A"):
        sumAge += age
        counter += 1
        
        minAge = min([minAge, age])
        maxAge = max([maxAge, age])

        ages.append(age)

    else:   
        sumAge -= age
        counter -= 1
        ages.remove(age)

        if(minAge == age and counter):
            minAge = min(ages)
        
        elif(maxAge == age and counter):
            maxAge = max(ages)

    if(counter):
        print(minAge, maxAge, sumAge/counter)
    else:
        print(-1, -1, -1)