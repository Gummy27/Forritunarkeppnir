daemi = list(input().split(";"))
teljari = 0
for x in daemi:
    if "-" in x:
        fra, til = map(int, x.split("-"))
        teljari += til-fra+1
    else:
        teljari += 1
print(teljari)