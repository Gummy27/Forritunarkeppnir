n = list(input())

delete = 0
for x in range(len(n), 0, -1):
    x -= 1
    if(n[x] == "<"):
        delete += 1
        n[x] = ''

    elif(delete):
        n[x] = ''
        delete -= 1

print(''.join(n))
