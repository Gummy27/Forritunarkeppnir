fjoldi = int(input())
blod = [x+1 for x in range(0, fjoldi, 2)]
while len(blod) > 1:
    boolean = len(blod) % 2 == 0
    blod = [x+1 for x in range(boolean, max(blod), 2)]
    print(blod)

'''
while len(blod) > 0:
    newList = []
    for x in blod:
        if boolean:
            boolean = not boolean
            newList.append(x)
            last = x
        else:
            boolean = not boolean
    blod = newList
print(x)
'''