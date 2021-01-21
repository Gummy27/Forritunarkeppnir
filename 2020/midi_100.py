n = int(input())

strengur = []
for x in range(n):
    strengur.append(input())
print(''.join(strengur)[::-1])