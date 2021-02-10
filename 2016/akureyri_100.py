from collections import defaultdict

n = int(input())

m = defaultdict(lambda : 0)
for x in range(n):
    _ = input()
    nafn = input()
    m[nafn] += 1

for x, y in m.items():
    print(x, y)