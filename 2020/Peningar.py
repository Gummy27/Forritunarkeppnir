from __future__ import print_function
n, d = map(int, raw_input().split(' '))
penge = list(map(int, raw_input().split(' ')))
penge.append('Stopp')

peningar = 0
reitur = 0
while True:
    if penge[reitur] != 'Stopp':
        peningar += penge[reitur]
    else:
        break

    reitur += d
    if reitur > n:
        reitur -= n

print(peningar)