l, r, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
cnt = 0

for tala in range(l, r+1):
    for fav in list(a):
        if tala % fav == 0:
            cnt += 1
            break

print(cnt)
