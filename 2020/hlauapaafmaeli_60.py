# Afmaelið hennar er 2020

ar = int(input())

cont = True

aldur = 0
if ar % 4 == 0:
    if ar % 100 == 0:
        if ar % 400 == 0:
            aldur = round((ar-2020)/4)
        else:
            print("Neibb")
            cont = False
    else:
        aldur = round((ar-2020)/4)
else:
    print("Neibb")
    cont = False

if cont:
    if ar - 2020 > 100:
        for x in range(2100, ar, 100):
            if x % 100 == 0 and x % 400 != 0:
                aldur -= 1
    print(aldur)
