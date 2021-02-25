def gini(moneys):
    pass

n = int(input())

people = []
for x in range(n):
    people.append(int(input()))

firstSum = 0
for x in range(n):
    for i in range(n):
        firstSum += abs(people[x] - people[i])

secondSum = 0
for x in range(n):
    for i in range(n):
        secondSum += people[x]

print(firstSum / (2*secondSum))