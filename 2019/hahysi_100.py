# n : Lengd
# m : breidd
# Hver reitur er 1 fermetri

n, m = map(int, input().split(' '))

a = (n*(n-1))//2
b = (m*(m-1))//2

print(a*b % (10**9+7))