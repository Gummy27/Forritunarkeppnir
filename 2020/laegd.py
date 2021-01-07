n, m = map(int, input().split(' '))

def valuesAround(x, y):
    cords = []
    cords.append([x, y+1])
    cords.append([x, y-1])
    cords.append([x+1, y])
    cords.append([x+1, y])

    return cords


pressure = []
for x in range(n):
    pressure.append(list(map(int, input().split(' '))))

cont = True
for xx in range(0, n):
    for yy in range(0, m):
        laegd = 0
        for x, y in valuesAround(xx, yy):
            if pressure[x][y] > pressure[xx][yy]:
                laegd += 1
            if laegd == 4:
                cont = False
                print("Jebb")
                break
        if not cont:
            break
    if not cont:
        break
if cont:
    print("Neibb")

