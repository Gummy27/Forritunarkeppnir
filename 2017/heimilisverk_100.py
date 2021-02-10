from collections import defaultdict

def value():
    return 0

chores = []
duplicate = defaultdict(value)

n = int(input())
for x in range(n):
    newChore = input()
    if not duplicate[newChore]:
        chores.append(newChore)
        duplicate[newChore] = 1

for x in chores:
    print(x)