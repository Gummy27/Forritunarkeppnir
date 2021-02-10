from collections import deque

n = int(input()) // 3
row = deque(sorted(map(int, input().split(" "))))

for x in range(n, 0, -1):
    temp = row[n+n-1]
    row.remove(temp)
    row.appendleft(temp)

for x in row:
    print(x, end=" ")
print()