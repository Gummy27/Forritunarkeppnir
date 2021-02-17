# n : Fjöldi gátta
n = int(input())

portals = list(range(1, n+1))

destinations = {}
prev = 1
for x in range(n):
    newDest = int(input())
    destinations[prev] = newDest
    prev = newDest

q = int(input())

for x in range(q):
    start, end = map(int, input().split(" "))

    current = int(start)

    counter = 0
    for i in range(n):
        counter += 1

        try:
            current = destinations[current]
        except:
            print(-1)
            break

        if(current == end):
            print(counter)
            break

        elif(current == start or x == n-1):
            print(-1)
            break
