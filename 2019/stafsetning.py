# n : Fjöldi dæma
# m : Fjöldi sekúnda sem tekur að lagfæra
# k : Fjöldi mínúta sem unnur getur eytt

n, m, k = map(int, input().split(' '))
s = list(map(int, input().split(' ')))

villur = []
for x in s:
    for i in range(x):
        villur.append(1*m)

index = 0
dagar = 1
if m <= k:
    while villur[-1] > 0:
        min = k
        while min > 0 and index < len(villur):
            if villur[index] <= min:
                min -= villur[index]
                villur[index] = 0
                index += 1
            else:
                dagar += 1
                break
    print(dagar)
else:
    print(":(")