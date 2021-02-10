x, y = map(int, input().split(" "))

if(1 in [x, y]):
    print(max([x, y])*2-2)
else:
    if(not(x%2 and y%2)):
        print(x*y)
    else:
        print(x*y+1)