n = int(input())

from math import sqrt, pow

def distance(cords1, cords2):
    return sqrt((cords1[0] - cords2[0])**2 + (cords1[1] - cords2[1])**2)

def recursive(cords, dist, current):
    if(len(cords) == 0):
        return dist + distance(current, [0, 0])

    else:
        smallestDist = 0
        for index, x in enumerate(cords):
            try:
                newCords = cords[0:index] + cords[index+1:]
            except:
                newCords = cords[0:-1]

            newDist = recursive(newCords, distance(current, x), x)
            
            if(smallestDist):
                smallestDist = min(smallestDist, newDist)
            else:
                smallestDist = newDist
                
        return dist + smallestDist

cords = []
maxX, maxY, minX, minY = 0, 0, 0, 0
for i in range(n):
    x, y = list(map(int, input().split(" ")))

    maxX = max(x, maxX)
    maxY = max(y, maxY)

    minX = min(x, minX)
    minY = min(y, minY)

    cords.append([x, y])

if(maxX == 0 and minX == 0):
    print(abs(maxY-minY)*2)
elif(maxY == 0 and minY == 0):
    print(abs(maxX-minX)*2)
else:
    print(recursive(cords, 0, [0, 0]))