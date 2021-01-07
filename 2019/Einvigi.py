# n : Fjöldi hermanna
# a : Styrkleiki hermanns.
# b : Stykleiki hermanns andstæðingsins.
# k : Styrkleiki ofurseyðis
# m : Fjöldi einvíga sem seyðið virkar.

from time import sleep

n, m, k = map(int, input().split(' '))
tomasHermenn = list(map(int, input().split(' ')))
andstHermenn = list(map(int, input().split(' ')))

def potion(hermenn, strength, rounds, pos):
    for x in range(pos, pos+rounds):
        try:
            hermenn[x] += strength
        except:
            pass
    return hermenn

def einvigi(tomasHermenn, andstHermenn):
    teljari = 0
    for tomas, andst in zip(tomasHermenn, andstHermenn):
        if tomas > andst:
            teljari += 1
        elif tomas < andst:
            teljari -= 1
    return teljari

teljari = einvigi(tomasHermenn, andstHermenn)
round = 0

if teljari < 0:
    for x in range(n):
        tempHermenn = potion(tomasHermenn, k, m, x)
        teljari = einvigi(tempHermenn, andstHermenn)
        if teljari > 0:
            round = x
            break


if teljari >= 0:
    print(round)
else:
    print("Neibb")