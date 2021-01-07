# r : Raðir
# d : Dálkar
# a, b : a-r b-d

r, d = map(int, input().split(' '))

if r % 3 == 0:
    for x in range(d):
        print(0, x)
    for x in range(1, r):
        for i in range(d-1):
            print(x, i)

    for x in range(r, 0):
        print(r, 0)