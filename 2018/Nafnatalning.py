# n : Magn af nafna pörum.
# p : Mörg pör af nöfnum á einum degi.
n, p = map(int, input().split(' '))
a = list(map(int, input().split()))

def iterateNr(name, nr):
    teljari = 0
    while name > 0:
        name -= nr
        teljari += 1
    return teljari

teljari = 0
for x in a:
    if x <= p:
        teljari += 1
    else:
        teljari += iterateNr(x, p)

print(teljari)



