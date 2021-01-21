nafn = input()
loka = input()

krakkar = 1
for x, y in zip(nafn, loka):
    if(x != y):
        krakkar += 1
print(krakkar)