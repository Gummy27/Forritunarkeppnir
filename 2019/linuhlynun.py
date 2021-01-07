# n : Fjöldi nemenda
# a og b : Húsanúmer

hus = []
n = int(input())
for x in range(n):
    hus.append(list(map(int, input().split(' '))))

co2 = 0
eydsla = []
for possible in range(min(hus)[0], max(hus)[0]+1):
    for student in hus:
        co2 += abs((possible - student[0]) * student[1])
    eydsla.append([co2, possible])
    co2 = 0

print(min(eydsla)[1])