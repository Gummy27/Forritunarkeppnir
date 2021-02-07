# Guðmundur Brimir Björnsson

input()
listi = list(map(int, input().split(' ')))
teljari = 0

'''
While lykkjan mun keyra þangað til að listinn er tómur. Í lykkjuni er stalínröðunin
framkvæmd. Fyrst er farið í gegnum listann með for lykkju. Nr breytan tekur á sig stak úr listanum.
Fyrst er gáð hvort að nr sé stærra en stærsta gildið. Ef svo er þá er sett í largest breytuni.
Ef að nr er minna en stærsta gildið þá er það sett í nýjan lista. Að þessu loknu er fær listinn
á sig nýja listan og while lykkjan heldur áfram. Þetta er gert þar til listinn er tómur. Þá er teljarinn
prentaður.
'''

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

