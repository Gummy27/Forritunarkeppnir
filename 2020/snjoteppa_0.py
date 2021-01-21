n, k = map(int, input().split(' '))
grid = [list(input()), list(input())]

fyrirspurninir = []
for x in range(k):
    fs = input().split(' ')

    if fs[0] == 'U':
        if grid[int(fs[1])-1][int(fs[2])-1] == '.':
            grid[int(fs[1]) - 1][int(fs[2]) - 1] = 'o'
        else:
            grid[int(fs[1]) - 1][int(fs[2]) - 1] = '.'
    else:
        if grid[0].count('o') == 0 or grid[1].count('o') == 0:
            print("Jebb")
        else:
            print("Neibb")

