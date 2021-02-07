# Guðmundur Brimir Björnsson

'''
Þetta dæmi var leyst með hjálp dict. Talan sem segir hve mikið manneskja er í mál er 
geymd í dict sem key og index manneskjurnar sem value. Þannig er hægt að raða listanum með key
og þnnig prenta öll gildin (index).
'''

d = {}
input() # Forritið þarf ekki fyrsta inntakið.
rod = list(map(int, input().split(" "))) # Röðin er splittuð í lista.

for x, y in enumerate(rod):
    d[y] = x+1 
    
listi = sorted(d, key=d.get, reverse=True)
for x in listi:
    print(x, end=" ")