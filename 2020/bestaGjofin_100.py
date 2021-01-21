n = int(input())

besta = 0
besta_nafn = ""
for x in range(n):
    nafn, stig = input().split(' ')
    if(int(stig) > besta):
        besta = int(stig)
        besta_nafn = nafn

print(besta_nafn)