from collections import deque

ages = deque([])

# Full af breytum eru frumstilltar.
sumAge, minAge, maxAge, counter = 0, 0, 0, 0
for x  in range(int(input())):
    action, age = input().split(" ")
    age = int(age)

    # Gáð er hvort að einhverjir eru í listanum.
    if(not counter):
        minAge = age
        maxAge = 0

    # Hérna er manneskju bætt við og aldri.
    if(action == "A"):
        sumAge += age
        counter += 1
        
        minAge = min([minAge, age])
        maxAge = max([maxAge, age])

        ages.append(age)

    # Hérna er manneskja eydd úr lista.
    else:   
        sumAge -= age
        counter -= 1
        ages.remove(age)

        if(minAge == age and counter):
            minAge = min(ages)
        
        elif(maxAge == age and counter):
            maxAge = max(ages)

    # Ef að einhverjir eru í listanum þá er prentaðar allar helstu upplýsingar.
    if(counter):
        print(minAge, maxAge, sumAge/counter)
    # Annars er bara prentað út -1 -1 -1.
    else:
        print(-1, -1, -1)