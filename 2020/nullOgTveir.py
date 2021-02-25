n = int(input())

for x in range(n, -1, -1):
    if(str(x).count('0') + str(x).count('2') == len(str(x))):
        highest = x
        break

print(highest)
print(str(highest).replace('2', '1'))
if(int(str(highest)[-1]) == 2):
    print(2**len(str(highest))+1)
else:
    print(2**len(str(highest)))
    
    
