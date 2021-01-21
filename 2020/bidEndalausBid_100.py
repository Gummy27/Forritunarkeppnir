fyrsta = list(map(int, input().split(":")))
annad = list(map(int, input().split(":")))

if annad[0] < fyrsta[0]:
    minutu = (24 - fyrsta[0] + annad[0])*60
else:
    minutu = (annad[0] - fyrsta[0]) * 60

minutu += annad[1] - fyrsta[1]

print(minutu)
