a, b, x, n, m = map(int, input().split(' '))

for i in range(n):
    x = (a*x+b)%m
print(x)