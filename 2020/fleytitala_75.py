vegalengd = float(input())
skopp = int(input())

temp = vegalengd
for x in range(skopp):
    temp /= 2.0
    vegalengd += temp
    

print(vegalengd)

