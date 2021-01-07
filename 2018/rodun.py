# n : Fjöldi keppenda
# k : Fjöldi samanburða

n, k = map(int, input().split(' '))
temp = input().split(' ')

nofn = []
for x in range(k):
    nofn.append(list(input().split()))

print(nofn)

