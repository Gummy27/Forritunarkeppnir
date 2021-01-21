n, d = map(int, input().split(' '))
penge = list(map(int, input().split(' ')))

peningar = 0
pos = 0
while(penge[pos]):
    peningar += penge[pos]
    penge[pos] = 0

    pos += d
    pos %= n

print(peningar)