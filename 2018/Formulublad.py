# i : Línur sem ein formúla tekur að skrifa
# m : Mikilvægisgildi formúlunnar.
# l : Línur sem komast á blaðið

n, l = map(int, input().split(' '))

formulur = []
for x in range(n):
    formulur.append(list(map(int, input().split(' '))))

math = []
for index, formula in enumerate(formulur):
    math.append([formula[1]/formula[0], formula[0], formula[1], index])

math.sort()
math = math[::-1]

linur, points, loka = 0, 0, []
for x in math:
    if linur + x[1] < l:
        points += x[2]
        loka.append(str(x[-1]))
        linur += x[1]
    elif linur + x[1] == l:
        points += x[2]
        loka.append(str(x[-1]))
        linur += x[1]
        break

loka.sort()
print(len(loka), points)
print(' '.join(loka))
