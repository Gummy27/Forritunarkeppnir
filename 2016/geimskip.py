from math import sqrt

def distance(obj1, obj2):
    return sqrt((obj2[0]-obj1[0])**2+(obj2[1]-obj1[1])**2+(obj2[2]-obj1[2])**2)

spaceship = []
for x in range(int(input())):
    spaceship.append(list(map(int, input().split(" "))))

blast = []
shotdown = 0
for x in range(int(input())):
    blast.append(list(map(int, input().split(" "))))

'''
while(blast):
    newBlast = []
    to_be_deleted = []

    for x in range(len(blast)):
        for i in range(len(spaceship)):
            if(distance(spaceship[i], blast[x]) <= blast[x][-1]+spaceship[i][-1]):
                temp = spaceship[i]
                temp[-1] *= 2
                newBlast.append(temp)
                to_be_deleted.append(i)

    for x in to_be_deleted:
        spaceship.pop(x)
    blast = newBlast
'''

newBlast = []
to_be_deleted = []

for x in range(len(blast)):
    for i in range(len(spaceship)):
        if(distance(spaceship[i], blast[x]) <= blast[x][-1]+spaceship[i][-1]):
            to_be_deleted.append(i)
for x in to_be_deleted:
    spaceship.pop(x)

print(len(spaceship))