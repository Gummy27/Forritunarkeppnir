password = input()
cursor = 0
decrypted = []

for x in password:
    if(x == "L"):
        cursor -= 1

    elif(x == "R"):
        cursor += 1

    elif(x == "B"):
        cursor -= 1
        decrypted.pop(cursor)

    else:
        decrypted.insert(cursor, x)
        cursor += 1

print(''.join(decrypted))