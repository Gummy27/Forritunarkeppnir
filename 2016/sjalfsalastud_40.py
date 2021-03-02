from math import ceil

bottles, p10, p50, p100 = map(int, input().split(" "))

price = bottles * 80
coins = 0
# Fyrst er reiknað út hve margir 100 kallar geta verið notaðir.
if(price >= 100):
    # Gáð er hvort að andvirði flaskanna er meiri en fjöldi 100 kalla sem við eigum.
    if(p100 > (bottles * 80) // 100):
        bottlesBought = (bottles * 80) // 100
        coins += (bottles * 80) // 100
    # Ef að flöskurnar eru færri en 100 kallarnir þá einfaldlega tekur bottlesbought og coins gildi p100.
    else:
        bottlesBought = p100
        coins += p100

    bottles -= bottlesBought
    leftover = 100 * bottlesBought - (bottlesBought * 80) 

    p50 += leftover // 50
    leftover -= leftover // 50
    p10 += leftover // 10

price = bottles * 80

# Þessi while lykkja keyrir þangað til að verð er komið í núll.
while(price):
    # Gáð er fyrst hvort að við eigum einhverja 50 kalla.
    if(p50):
        # Síðan er gáð hvort að 50 kallarnir eru sama eða fleiri en 2.
        if(p50 >= 2 and p50 >= ceil(price / 50)):
            # Hér er borgað með 2 50 köllum og maður fær 2 10 kalla til baka.
            p50 -= 2
            p10 += 2
            coins += 2
            price -= 80
        # Hér er borgað með einum 50 kalli og þremur 10 köllum.
        else:
            p50 -= 1
            p10 -= 3
            coins += 4
            price -= 80
    else:
        coins += price // 10
        break

print(coins)