n = int(input())

longest = 0
matrix = []
# Farið er í gegnum öll inputin og lengsti strengurinn er fundinn.
for x in range(n):
    temp = list(input())
    if(len(temp) > longest):
        longest = len(temp)
    
    matrix.append(temp)

# Hér er farið í gegnum alla strengina.
for x in range(longest):
    # Hér er farið i gegnum alla stafina í strengjunum með indexið x
    for i in range(n):
        # Hér er notað try og except aðgerð til að prenta út stafina. 
        try:
            print(matrix[i][x], end="")
        # Ef að villa kemur upp þá prentar forritið út auðu.
        except:
            print(end=" ")
    print()
