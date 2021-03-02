input("think of a number in the range 1-100 and press a key when ready")
min = 1
max = 100
while(True):
    cpguess = (max-min)//2 + min
    useranswer = input("Is this your number? "+ str(cpguess) + "\n please type Y for yes, H if the number is too high, L if the number is too low ")
    if (useranswer == "Y"):
        print("Yay, I guessed the number")
        break
    elif (useranswer == "H"):
        max = cpguess
    elif (useranswer == "L"):
        min = cpguess
    else:
        print("Your answer is invalid. Please follow the instructions") 
       
   
   
   
    
   
   
   

