import math
print("This program will allow the user to give a number to the machine\n\
and it will return the addition of its digits.")

try:
    x = float(input("Give me a number: "))
    #Xrhsimopoiw thn apoluth timh jathws eite 8etikos eite arnhtikos to athroisma paramenei idio
    #Triplasiazw kai prosthetw mia monada opws apaitei h ekfwnhsh
    y = round(abs(3*x+1))

    #emfanizei minima gia epivevaiosh toy arithmou
    print("The number that is going to be calculated is: ",y)
    if x >= 3 :
        i = 0 #metrhths

    #metraw ta pshfia toy arithmoy(se plhthos)
        while y >= 10 :                          
            i += 1
            y /= 10 
            #print(y,i)

        value = round(abs(3*x+1))
    #Kataxwrw se enan pinaka ta pshfia toy ena pros ena diairontas ton me deka 
        athroisma_pshfion = 0
        for j in range(i):
            upoloipo = math.fmod(value,10)
            phliko = (value-upoloipo)/10
            pshfio = value - phliko*10
            value = phliko
            athroisma_pshfion += pshfio
            if j == i-1 :
                athroisma_pshfion += value
        print("The addition of the number 's digits is: ", athroisma_pshfion)
                
            
    else :
        print("The addition of the number 's digits is: ",y)
except ValueError:
    print("Invalid entry!")
