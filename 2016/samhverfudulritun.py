# 45 0.71s

def isPalindrome(number):
    if(number[0] == number[-1]):
        odd = 0
        if(not len(number) % 2):
            odd = 1
        
        middle = len(number)//2 - odd
        for x in range(1, middle+1+odd):
            if(number[middle-x+odd] != number[middle+x]):
                return 0
        return number
    else:
        return 0

for k in range(1, 45):
    biggestPalindrome = 0
    for i in range(2**k, k, -1):
        i = str(i)
        palindrome = isPalindrome(i)
        if palindrome:
            break
    print(k, palindrome)