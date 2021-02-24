import sys

def removeFromMatrix(value, matrix):
    for firstIndex, nested in enumerate(matrix):
        for secondIndex in range(len(nested)):
            if nested[secondIndex] == value:
                nested.pop(secondIndex)
                break
    
    return matrix

n = int(input())

sizes = []
for x in range(n):
    sizes.append(list(map(int, input().split(" "))))

possible = []
tShirt = list(map(int, input().split(" ")))

for lowest, highest in sizes:
    temp = []
    for x in tShirt:
        if(lowest <= x and x <= highest):
            temp.append(x)
    if(temp):
        possible.append(temp)
    else:
        print("Neibb")
        sys.exit()

while(possible):
    tempPossible = possible
    offset = 0
    for index, x in enumerate(possible):
        if(len(x) == 1):
            possible.pop(index+offset)
            offset -= 1
            possible = removeFromMatrix(x[0], possible)
        elif(len(x) == 0):
            possible.pop(index+offset)
            offset -= 1

    for index, x in enumerate(possible):
        temp = possible[:index:] 
        if(x and possible.count(x) > 1):
            if(possible.count(x) == len(x)):
                for valueToDelete in list(x):
                    possible = removeFromMatrix(valueToDelete, possible)
            elif(possible.count(x) > len(x)):
                print("Neibb")
                sys.exit()
    
    if(tempPossible == possible):
        print("Neibb")
        sys.exit()
print("Jebb")

