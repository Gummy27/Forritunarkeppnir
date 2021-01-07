n, m = map(int, input().split(' '))
highest = 0
painted = 0
for x in range(m):
    i, j = map(int, input().split(' '))
    if i > highest:
        highest = j
        painted += j - i

    else:
        painted += j - highest

print(painted)
if n/2 < painted:
    print("The Mexicans took our jobs! Sad!")

else:
    print("The Mexicans are Lazy! Sad!")





