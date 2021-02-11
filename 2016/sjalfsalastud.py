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

if(price >= 50):
    if(p50 > (bottles * 80) // 50):
        bottlesBought = (bottles * 80) // 50
        coins += (bottles * 80) // 50
    else:
        bottlesBought = p50
        coins += p50

    bottles -= bottlesBought
    leftover = 50 * bottlesBought - (bottlesBought * 80) 

    p10 += leftover // 10

if(price >= 10):
    coins += (bottles * 80) // 10

print(coins)