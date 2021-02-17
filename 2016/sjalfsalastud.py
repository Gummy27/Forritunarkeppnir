from math import ceil

bottles, p10, p50, p100 = map(int, input().split(" "))

price = bottles * 80

coins = 0
if(price >= 100):
    if(p100 > (bottles * 80) // 100):
        bottlesBought = (bottles * 80) // 100
        coins += (bottles * 80) // 100
    else:
        bottlesBought = p100
        coins += p100

    bottles -= bottlesBought
    leftover = 100 * bottlesBought - (bottlesBought * 80) 

    p50 += leftover // 50
    leftover -= leftover // 50
    p10 += leftover // 10

price = bottles * 80

while(price):
    if(p50):
        if(p50 >= 2 and p50 >= ceil(price / 50)):
            p50 -= 2
            p10 += 2
            coins += 2
            price -= 80
        else:
            p50 -= 1
            p10 -= 3
            coins += 4
            price -= 80
    else:
        coins += price // 10
        break

print(coins)