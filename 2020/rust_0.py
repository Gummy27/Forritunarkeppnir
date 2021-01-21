n, k = map(int, input().split(' '))
grid = []
for x in range(n):
    grid.append(list(input()))

def valuesAround(x, y):
    cords = []
    cords.append([x, y+1])
    cords.append([x, y-1])
    cords.append([x+1, y])
    cords.append([x-1, y])
    cords.append([x+1, y+1])
    cords.append([x+1, y-1])
    cords.append([x-1, y-1])
    cords.append([x-1, y+1])
    cords.append([x, y])
    return cords

verdmaedast = []
for x in range(1, n-1):
    for y in range(1, n-1):
        verdmaeti = 0
        for xx, yy in valuesAround(x, y):
            try:
                verdmaeti += int(grid[xx][yy])
            except:
                if grid[xx][yy] == "#":
                    print(verdmaeti, end=" ")
                    verdmaeti = 0
                    print(verdmaeti)
                    break
        verdmaedast.append(verdmaeti)

print(max(verdmaedast))

