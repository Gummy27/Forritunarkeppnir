path = list(input())

backpack = []
flag = 0
for x in path:
    if(x not in ["P", "G", "O"]):
        if(x != "."):
            backpack.append(x)
    else:
        if(len(backpack) == 0):
            print("Neibb")
            exit()
        for i in range(len(backpack)-1, -1, -1):
            if(backpack.pop(i) == x.lower()):
                break

            elif(len(backpack) == 0):
                print("Neibb")
                exit()

print(backpack.count('p'))
print(backpack.count('g'))
print(backpack.count('o'))
    