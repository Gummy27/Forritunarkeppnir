lengd, breidd = map(int, input().split(" "))
sprengjur = []
teljari = 0
for y in range(lengd):
    listi = list(input())
    for x, i in enumerate(listi):
        if i == "*":
            teljari += 1
            sprengjur.append(str(y+1)+" "+str(x+1))
print(teljari)
for x in sprengjur:
    print(x)