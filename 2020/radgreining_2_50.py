n, m = map(int, input().split(" "))

def recursive(sequence, pieces):
    if(len(pieces) == 0):
        return sequence, False

    else:
        for x in range(1, -2, -2):
            index, piece = pieces[0]

            newSequence = list(sequence)
            index = int(index) - 1
            piece = piece[::x]

            flag = False
            for i in range(len(piece)):
                if(newSequence[i+index] == "" or newSequence[i+index] == piece[i]):
                    newSequence[i+index] = piece[i]
                else:
                    flag = True
                    break

            if(not flag):
                returnedSequence, failure = recursive(newSequence, pieces[1:])
                if(not failure):
                    return returnedSequence, False

        return newSequence, True


pieces = []
for x in range(m):
    pieces.append(list(input().split(" ")))

sequence, failure = recursive(['']*n, pieces)
if(not failure):
    for x in range(len(sequence)):
        if(sequence[x] == ''):
            sequence[x] = "T"
    
    print(''.join(sequence))
else:
    print("Villa")

