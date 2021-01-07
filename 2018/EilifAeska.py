# i : Glasið sem hellt er
# j : Glasið sem verið er að fylla
n = int(input())
glos = list(map(int, input().split(' ')))

def jafnt(numbers):
    return sum(numbers) / len(numbers)

target = jafnt(glos)

if n == 1:
    print(0)
    print(1)

elif n == 2:
    print(1)
    if glos[0] > glos[1]:
        print(1, 2)
    else:
        print(2, 1)





