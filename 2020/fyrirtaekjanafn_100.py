serhljothar = ["a", "e", "i", "o", "u", "y"]

n = input()

nytt_nafn = []
for x in n:
    if x.lower() in serhljothar:
        nytt_nafn.append(x)

print(''.join(nytt_nafn))