# n : Fjöldi dæma
# m : Fjöldi sekúnda sem tekur að lagfæra
# k : Fjöldi mínúta sem unnur getur eytt

n, m, k = map(int, input().split(' '))
s = list(map(int, input().split(' ')))

if(m > k):
    print(":(")

else:
    a = k // m
    print(int((sum(s) + a - 1) // a))