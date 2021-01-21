n, m = map(int, input().split(' '))

def valuesAround(x, y):
    og = pressure[x][y]

    cords = 0
    cords += og < pressure[x][y+1]
    cords += og < pressure[x][y-1]
    cords += og < pressure[x+1][y]
    cords += og < pressure[x-1][y]

    if cords == 4:
        return True
    else:
        return False


pressure = []
for x in range(n):
    pressure.append(list(map(int, input().split(' '))))

flag = False
for x in range(1, n-1):
    for y in range(1, m-1):
        if valuesAround(x, y):
            print("Jebb")
            flag = True
            break
    if flag:
        break

if not flag:
    print("Neibb")

