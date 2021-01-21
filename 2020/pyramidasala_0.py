n, m = map(int, input().split(' '))

starfsmenn = []
for x in range(3):
    starfsmenn.append(list(input().split(' ')))


yfirmadur = starfsmenn[0][0]

complete = [[]]*n

undirmenn = []

undir = ''.join(starfsmenn[1]).split(yfirmadur)
undirundir = []
for x in undir:
    if len(x) == 1:
        yfir = x
    else:
        yfir = x[1]

    undirundir += list(x.replace(yfir, ''))
    complete[int(yfir)-1] = list(x.replace(yfir, ''))



for x in range(len(complete)):
    print(str(x+1)+':', ' '.join(complete[x]))

