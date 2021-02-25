from math import factorial, pow

equation = lambda x : ((x * 230309227) + 68431307) % 2**64

perfectNumbers = [
    6,
    28,
    496,
    8128,
    33550336,
    8589869056,
    137438691328,
    2305843008139952128,
    2658455991569831744654692615953842176,
    191561942608236107294793378084303638130997321548169216
]

for x in range(100):
    encrypted = int(input())
    flag = False
    # Minna en 1000 og 10
    for x in range(1000):
        if equation(x) == encrypted:
            print(x)
            flag = True
            break

    # Perfect numbers
    if(not flag):
        for x in perfectNumbers:
            if equation(x) == encrypted:
                print(x)
                flag = True
                break
    if(not flag):
        # Factorial numbers
        for x in range(50):
            if(equation(factorial(x)) == encrypted):
                print(x)
                flag = True
                break

    if(not flag):
        # 2**n
        for x in range(100):
            if(equation(2**x) == encrypted):
                print(x)
                flag = True
                break
    
    if(not flag):
        # Fibonacci number
        fibonacci = 1
        prev = 1
        while(fibonacci > 10**8):
            temp = fibonacci
            fibonacci += prev
            prev = temp

            if(equation(factorial(fibonacci)) == encrypted):
                print(x)
                flag = True
                break

    if(not flag):
        # Catalan number
        catalan = lambda x : factorial(2*x) / (factorialx+1)*factorial(x)
        for x in range(100):
            pass
    
    if(not flag):
        # Motzkin number
        for x in range(100):
            pass
    
    if(not flag):
        # Triangular number
        for x in range(100):
            pass
    
    if(not flag):
        # Big bois < 10**18
        for x in range(100):
            pass

    if(not flag):
        print(0)