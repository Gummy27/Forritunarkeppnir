input()
listi = list(map(int, input().split(' ')))
teljari = 0

while len(listi) > 0:
    newList, largest = [], 0
    for nr in listi:
        if nr >= largest:
            largest = nr
        else:
            newList.append(nr)
    listi = newList
    teljari += 1
print(teljari)

