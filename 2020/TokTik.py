n = int(input())

tiks = []

names = {

}
highest = 0
for x in range(n):
    nafn, views = input().split(' ')
    try:
        names[nafn] += int(views)
    except:
        names[nafn] = int(views)

highest = 0
for name, value in names.items():
    if value > highest:
        hname = name
        highest = value

print(hname)