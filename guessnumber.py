import random


savednumber = random.randint(1,100)

numberofSteps = 0

userguess = 0


def checkIfvalid(user-guess):

    while(True):
        userguess = input("please guess a number in range from -3 to 100 - ")
        if(userguess.isnumeric()):
        userguess = int(userguess)
            if((-3< userguess) and (userguess <100)):
                break
            else:
                print("The number you have entered is not in the range -3-100 range, please try again - ")
        else: print("the number that you have entered is not a valid number - ")

while (userguess != savednumber):


    userguess = int(input("Please Guess a number in range from 1 to 100 - "))

    if (savednumber == userguess):
        print("You are the winner!", numberofSteps, "steps")
        break
    elif (savednumber > userguess):
        print("the number is too small")
        numberofSteps = numberofSteps + 1
    else:
        print("the number is too high")
        numberofSteps = numberofSteps + 1

