import sys

n = int(input())
m = list(map(int, input().split(' ')))

if(sum(m) == n):
    print(sum(m)-1)
    sys.exit()

first = m.index(0)
last = n - m[::-1].index(0)

best = 0
for i in range(first, last+1):
    for j in range(i, last+1):
        flip = m[i:j].count(0) - m[i:j].count(1)
        newBest = sum(m) + flip
        best = max([newBest, best])
print(best)
