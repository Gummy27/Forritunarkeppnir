n = int(input())

longest = 0
matrix = []
for x in range(n):
    temp = list(input())
    if(len(temp) > longest):
        longest = len(temp)
    
    matrix.append(temp)

for x in range(longest):
    for i in range(n):
        try:
            print(matrix[i][x], end="")
        except:
            print(end=" ")
    print()
