fjoldi = int(input())
skyttur1 = list(input())
skyttur2 = list(input())
for x in range(fjoldi):
    if skyttur1[x] == skyttur2[x]:
        print(0, end="")
    else:
        print(1, end="")