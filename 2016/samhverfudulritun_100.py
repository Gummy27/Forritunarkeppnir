# Nær 100 stigum á aðeins 0.06s
# Farið verður í gegnum allar tölurnar frá 1 til 100.
for k in range(1, 101):
    # Hæsta mögulega gildið er vistað.
    highest = 2**k
    if(len(str(highest)) == 1):
        print(k, highest)

    '''
    Svo hvernig þetta algrím virkar er að við förum aðeins í gegnum helming
    tölunar í einu. 

    t.d. 321123 er samhverfa en til að búa til þessa tölu þurfum við aðeins 
    321 þar sem restinn af tölunni er 321 bara snúið við. Þannig er hægt að 
    helminga þann tíma sem þarf til að finna hæstu samhverfuna með því að taka
    helming hæstu tölunar og keyra niður hana.
    '''

    elif(len(str(highest)) % 2 == 0):
        middle = len(str(highest))//2

        half = int(str(highest)[0:middle])

        for x in range(half):
            palindrome = int(str(half-x)+str(half-x)[::-1])
            if(palindrome <= highest):
                print(k, palindrome)
                break
    
    else:
        middle = len(str(highest))//2

        half = int(str(highest)[0:middle+1])

        for x in range(half):
            palindrome = int(str(half-x)+str(half-x)[:-1][::-1])
            if(palindrome <= highest):
                print(k, palindrome)
                break