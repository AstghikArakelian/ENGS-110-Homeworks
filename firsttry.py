
import random

def checkIfNumber(user_guess):
    if(user_guess.isnumeric()):
        return True
    else:
        print("The number that you have entered is not a valid number.")
        return False

def checkIfInRange(user_guess):
    if( (1 <= user_guess) and (user_guess <= 100)):
        return True
    else:
        print("The number you have entered is not in the 1-100 range, please try again")
        return False

def getValidValue():
    while(True):
        UserGuess = input("Please guess a number in range from 1-100: ")
        if(checkIfNumber(UserGuess)):
            UserGuess = int(UserGuess)
            if(checkIfInRange(UserGuess)):
                return UserGuess
