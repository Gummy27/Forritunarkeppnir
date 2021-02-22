from collections import defaultdict

q = int(input())
n = int(input())

problems = list(input().split(" "))

points = [0]*q
for x in range(n):
    for index, i in enumerate(list(input().split(" "))):
        points[index] += int(i)

print(problems[points.index(max(points))])