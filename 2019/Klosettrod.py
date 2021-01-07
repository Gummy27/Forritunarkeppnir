d = {}
input()
rod = list(map(int, input().split(" ")))
for x, y in enumerate(rod):
    d[y] = x+1
listi = sorted(d, key=d.get, reverse=True)
for x in listi:
    print(x, end=" ")