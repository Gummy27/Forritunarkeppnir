# n : Lengd strengsins dna

n, m = map(int, input().split(' '))
dna = []

complete = ['?']*n
cont = True
for x in range(m):
    start, dna = input().split(' ')
    print(start, dna)
    if cont:
        for index, i in enumerate(range(int(start), int(start)+len(dna))):
            if complete[i-1] == '?':
                complete[i-1] = dna[index]
            elif complete[i-1] != dna[index]:
                print("Villa")
                cont = False
                break

if cont:
    print(''.join(complete))
