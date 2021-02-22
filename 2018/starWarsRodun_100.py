n = int(input()) // 3

# N er lengd strengsins deilt með 3

row = list(map(str, sorted(map(int, input().split(" ")))))

'''
Frekar einföld lausn er bara að gera þrjár prent skipanir.
Sú fyrsta mun skrifa strengin frá n til n*2
Næsta mun skrifa strengin frá 0 til n
Og síðast mun skrifa strengin frá n*2 til enda.
'''
print(' '.join(row[n:n*2]), end=" ")
print(' '.join(row[0:n]), end=" ")
print(' '.join(row[n*2:]))
