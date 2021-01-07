fjoldi, taska = map(int, input().split(" "))
listi = list(map(int,input().split(" ")))
for x, y in enumerate(listi):
    if y == taska:
        if x == 0:
            print("fyrst")
        elif x == 1:
            print("naestfyrst")
        else:
            print(x+1, "fyrst")