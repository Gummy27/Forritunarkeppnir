n = int(input())
m = list(map(int, input().split(' ')))

def bitFlip(i, j):
    newList = list(m)
    for x in range(i, j):
        newList[x] = not newList[x]
    return sum(newList)

best = 0
for i in range(1, n):
    for j in range(i+1, n):
        newBest = bitFlip(i, j)
        if newBest > best:
            best = newBest
print(best)
