from math import sqrt

# [Phi**n – (phi)**n] / Sqrt[5].
def fibonacci(number):
    phi_1 = ( 1 + sqrt(5) ) / 2
    phi_2 = ( 1 - sqrt(5) ) / 2

    return float((phi_1**number - phi_2**number) / sqrt(5))


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
        print("These are the s")
        for x in numbers[l-1:r]:
            print(x, fibonacci(x))
            out += fibonacci(x)
        
        #22704730358999870804252323
        print("This is the output", out, out%(10**9+7))
'''