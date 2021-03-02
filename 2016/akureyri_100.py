from collections import defaultdict

n = int(input())

# Fyrst er smíðað default dict svo hægt sé að frumstilla stak með 0.
m = defaultdict(lambda : 0)
for x in range(n):
    input() # Fyrsta inputið er óþarfi svo ég tek það ekki  inn.
    m[input()] += 1 # Bærinn er settur í dict og hækkað um einn.

# Síðar eru öll bæjarfélögin prentuð út með tölunum.
for x, y in m.items():
    print(x, y)