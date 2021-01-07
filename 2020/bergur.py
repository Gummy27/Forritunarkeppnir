n = int(input())
listi = list(map(int, input().split(' ')))

time = listi.copy()

timi = 0
for dagur in listi:
    if dagur == min(time):
        timi += min(time)
        time.pop(0)
    else:
        timi += min(time)
        for index, x in enumerate(time):
            if dagur == x:
                time.pop(index)
                break

print(timi)
