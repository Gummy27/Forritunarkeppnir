n = list(input())

delete = 0 # Breytan delete er frumstillt og verður notuð til að eyða nokkrum stöfum í röð.
for x in range(len(n), 0, -1):
    x -= 1
    # Gáð er hvort að stakið sé "<"
    if(n[x] == "<"):
        # Delete breytan er hækkuð um einn.
        delete += 1
        n[x] = ''

    # Gáð er hvort að þurfi að eyða einhverju.
    elif(delete):
        n[x] = '' # Stakið er eytt.
        # Delete breytan er lækkuð um einn.
        delete -= 1

print(''.join(n))
