user_input = input("Input f|a|b (fibonacci, abundant or both): ")

#Upphafstölurnar í Fibonacci röðinni
fib1 = 0
fib2 = 1


if user_input == "f" or user_input == "b":
    fib_length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:\n-------------------")
    print(fib1) 
    print(fib2) # Fyrstu 2 tölurnar prentast alltaf, sama hvað inputið er
    for num in range(fib_length-2): #Dreg 2 frá fib_length vegna þess að það er þegar búið að prenta fyrstu 2 tölurnar
        fib3 =  fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        print(fib3)

if user_input == "a" or user_input == "b":
    max_abundant = int(input("Input the max number to check: "))
    print("Abundant numbers:\n-----------------")

    for num in range(1,max_abundant+1): #Metur allar tölur uppað og með hámarkinu sem á að athuga
        number_sum = 0 #Endursetur alltaf summuna á milli hverrar ítrunar

        for i in range(1,num): 
            if num % i == 0: #Metur hverja tölu og hvert hún sé eiginlegur deilari
                number_sum += i
        if number_sum > num: #Ef summa allra eiginlega deilara er hærri en núverandi tala sem verið er að skoða er hún prentuð
            print(num)


