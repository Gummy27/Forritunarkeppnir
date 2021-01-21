n, m = map(int, input().split(' '))

directions = []
for x in range(n):
    directions.append(input())
q = int(input())

# x : R0ð reitsins sem þjarkurinn byrjar á
# y : Táknar dálk reistins sem þjarkurinn byrjar á
# k : Fjöldi skrefa

for ll in range(q):
    x, y, k = map(int, input().split(' '))
    x -= 1
    y -= 1
    for _ in range(k):
        direction = directions[x][y]
        if direction == '<':
            y -= 1
        elif direction == '>':
            y += 1
        elif direction == '^':
            x -= 1
        elif direction == 'v':
            x += 1
    print(x+1, y+1)

