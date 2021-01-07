# v : upphafshraðinn
# a : hröðun
# t : tími
# d : Vegalengd

v, a, t = map(int, input().split(' '))

number = str(round((v*t)+0.5*a*t*t, 10))
main, auka = number.split('.')

print(main+'.'+auka+'0'*(9-len(auka)))