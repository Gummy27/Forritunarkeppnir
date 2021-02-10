n = int(input()) // 3
row = list(map(str, sorted(map(int, input().split(" ")))))

print(' '.join(row[n:n*2]), end=" ")
print(' '.join(row[0:n]), end=" ")
print(' '.join(row[n*2:]))
