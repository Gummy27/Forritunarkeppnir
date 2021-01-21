n = int(input())

boolValues = {}

prompts = []
for x in range(n):
    prompts.append(input().split(' '))

for prompt in prompts:
    if(prompt[0] == "INNTAK"):
        if(prompt[2] == "SATT"):
            boolValues[prompt[1]] = True
        else:
            boolValues[prompt[1]] = False

    elif(prompt[0] == "UTTAK"):
        if(boolValues[prompt[1]]):
            print(prompt[1], "SATT")
        else:
            print(prompt[1], "OSATT")

    elif(prompt[0] == "OG"):
        boolValues[prompt[3]] = boolValues[prompt[1]] and boolValues[prompt[2]]

    elif(prompt[0] == "EDA"):
        boolValues[prompt[3]] = boolValues[prompt[1]] or boolValues[prompt[2]]

    elif(prompt[0] == "EKKI"):
        boolValues[prompt[2]] = not boolValues[prompt[1]]