input()
buildings = tuple(map(int, input().split(' ')))
teljari = []
spenna, largest = 0, 0

for listi in [buildings, buildings[::-1]]:
    for building in listi:
        if building > largest:
            if spenna == 0 and largest != 0:
                spenna += 2
            elif largest != 0:
                spenna += 1
            largest = building
        else:
            teljari.append(spenna)
            largest, spenna = building, 0
teljari.append(spenna)

print(max(teljari))


