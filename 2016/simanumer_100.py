# N er fjöldi símanúmera í safninu.
from collections import Counter

teljari = Counter()
    
n = int(input())

for x in range(n):
    simanumer = input()
    for i in range(7):
        teljari[simanumer[:i]] += 1

q = int(input())

matches = []
for x in range(q):
    fyrirspurn = input()
    matches.append(teljari[fyrirspurn])

for x in matches:
    print(x)
    
