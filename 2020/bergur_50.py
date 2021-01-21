dagar=int(input())
listi=list(map(int,input().split()))

for i in range(dagar - 2, -1, -1):
    listi[i] = min(listi[i], listi[i + 1])
    print(listi)

print(sum(listi))