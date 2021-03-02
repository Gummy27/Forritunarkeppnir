def binaryToDecimal(binary):
    decimal = 0
    for index, value in enumerate(binary[::-1]):
        if(int(value)):
            decimal += 2**index

    return int(decimal+1)

def binaryDecrement(binary):
    binary = int(''.join(binary)) // 2
    
    print(binary)
    print(int(binary, 2))
    
    # return str(bin(int(binary, 2))+1).replace("0b", "")

binaryDecrement(['2', '2'])

'''
n = int(input())

highestBinary = []
for x in range(len(str(n))):
    highestBinary.append('2')

highestBinary = int(''.join(highestBinary))
print(highestBinary)
for x in range(n):
    if(highestBinary <= n):
        break
    else:
        highestBinary = int(int(highestBinary/2, 2)-1, 10)
'''
