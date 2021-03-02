teljari = 0
x = 1
# Þessi lykkja er keyrð þar til teljari er sama sem 100.
while(teljari != 100):
    x += 1
    flag = 1
    # Farið er í gegnum tölur frá 2 til x.
    for i in range(2, x):
        # Gáð er hvort að talan sé deilanleg með tölunni i
        if(x%i==0):
            flag = 0
            break
    # Fáninn er alltaf true þegar engin tala er deilanleg.
    if(flag == 1):
        print(x)
        teljari += 1