# Nær 100 stigum á aðeins 0.06s
for k in range(1, 101):
    highest = 2**k
    if(len(str(highest)) == 1):
        print(k, highest)

    elif(len(str(highest)) % 2 == 0):
        middle = len(str(highest))//2

        half = int(str(highest)[0:middle])

        for x in range(half):
            palindrome = int(str(half-x)+str(half-x)[::-1])
            if(palindrome <= highest):
                print(k, palindrome)
                break
    
    else:
        middle = len(str(highest))//2

        half = int(str(highest)[0:middle+1])

        for x in range(half):
            palindrome = int(str(half-x)+str(half-x)[:-1][::-1])
            if(palindrome <= highest):
                print(k, palindrome)
                break