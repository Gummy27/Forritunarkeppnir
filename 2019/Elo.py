# x : Byrjunar Elo
# n : Fjöldi spilara
# a
from time import sleep
n, arnar = map(int, input().split(' '))

limit = 0
spilarar = []
for x in range(n):
    spilarar.append(list(map(int, input().split(' '))))
    if spilarar[x][1] > limit:
        limit = spilarar[x][1]

while arnar <= limit:
    available, highest = [], 0
    for sp in spilarar:
        if sp[0] <= arnar and sp[1] >= arnar:
            available.append([sp[1], sp[2]])
            if sp[1] > highest:
                highest = sp[1]

    available.sort()
    target = available.pop()
    if (target[0] - arnar) % target[1] == 0:
        arnar += target[1]
    else:
        for x in available:
            pass

print(arnar)
