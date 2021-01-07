# b : breidd
# h : hæð
# n : fjöldi veggspjalda
# x1, x2 : x hnit
# y1, y2 : y hnit
from time import sleep


b, h, n = map(int, input().split(' '))

graph = []
for x in range(b+1):
    graph.append(['*']*(h+1))


# graph = list([[0]*(b+1)]*(h+1))
for x in range(n):
    # cords = list(map(int, input().split(' '))))
    x1, x2, y1, y2 = map(int, input().split(' '))
    graph[x1][y1] = 'x'
    graph[x2][y2] = 'x'
    graph[x1+x1][y1] = 'x'
    graph[]

for x in graph:
    print(x)
#print(cords)