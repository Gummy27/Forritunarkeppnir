password = input()

# Cursor breytan verður notuð til að geyma staðsetningu bendilsins.
cursor = 0

# Afkóðaða lykilorðið verður geymt í þessari breytu
decrypted = []

for x in password:
    if(x == "L"):
        # Ef að x er L þá þýðir að bendillinn fer til vinstri.
        cursor -= 1

    elif(x == "R"):
        # Ef að x er R þá þýðir að bendillinn fer til hægri.
        cursor += 1

    elif(x == "B"):
        # Ef að x er B þá þýðir að bendillinn fer til baka um einn og stak er eytt úr decrypted.
        cursor -= 1
        decrypted.pop(cursor)

    else:
        # Annars er staki bætt við í decrypted og bendillinn hækkar um einn.
        decrypted.insert(cursor, x)
        cursor += 1

print(''.join(decrypted))