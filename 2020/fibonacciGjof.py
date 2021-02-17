from math import sqrt
from decimal import *

getcontext().prec = 9

# [Phi**n – (phi)**n] / Sqrt[5].
def fibonacci(number):
    sqrt_5 = Decimal(sqrt(5))

    phi_1 = Decimal(( 1 +  sqrt_5) / 2)
    phi_2 = Decimal(( 1 - sqrt_5 ) / 2)

    print(Decimal(phi_1**number))
    print(phi_2**number)

    return Decimal((phi_1**number - phi_2**number) / sqrt_5)

print("2427893228399975082453")
print(fibonacci(104))
'''
n, m = map(int, input().split())

numbers = list(map(int, input().split(" ")))

for x in range(m):
    action = list(map(int, input().split(" ")))

    if(action[0] == 1):
        l, r, d = action[1:]

        for x in range(l-1, r):
            numbers[x] += d

    else:
        l, r = action[1:]

        out = 0
        for x in numbers[l-1:r]:
            out += fibonacci(x)
        
        #22704730358999870804252323
        print(out%(10**9+7))
'''