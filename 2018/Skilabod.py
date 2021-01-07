# d : Eininginn sem sendir drífur
from math import pow, sqrt

hnit, styrkur = [], []
for x in range(int(input())):
    hnit.append(list(map(int, input().split(' '))))

for x in range(int(input())):
    styrkur.append(int(input()))

for styrkleiki in styrkur:
    teljari = 0
    for x, y in hnit:
        fjarlaegd = sqrt(pow(x, 2)+pow(y, 2))
        if fjarlaegd < styrkleiki:
            teljari += 1
    print(teljari)
