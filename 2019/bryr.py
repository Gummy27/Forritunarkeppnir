# n : Fjöldi staða
# m : Fjöldi vega
# a : Frá
# b : Til
# c : 0 ef að er einbreið brú

n, m = map(int, input().split(' '))

vegir, start = [], []
for x in range(m):
    vegir.append(list(map(int, input().split(' '))))
    if vegir[x][0] == 1 or vegir[x][1] == 1:
        print(vegir[x])

print(start)
print(vegir)

'''
for a, b, c in start:
    d = max([a, b])
    for x in 
'''
