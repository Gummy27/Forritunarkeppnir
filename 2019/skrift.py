# n er lengd orðsins
# m eru fjöldi ólíkra bókstafa
# q er fjöldi aðgerða
n, m, q = map(int, input().split(" "))

letters = []
for x in range(m):
    # a hve mörgum sinnum bókstafurinn kemur fram. b stærð
    a, b = map(int, input().split(" "))
    for x in range(a):
        letters.append(b)

letters = sorted(letters)[::-1]

erase = 0
for x in range(q):
    # x: 1 hann skrifar y stafi. 2 hann strokar út y stöfum.
    x, y = map(int, input().split(" "))
    if(x == 2):
        erase += y

print(sum(letters[0:erase]))