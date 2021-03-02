
def checkIfNumber(user_number):
    if(user_number.isnumeric()):
        return True
    else:
        print("The number that you have entered is not a valid number.")
        return False

def checkIfpositive(user_number):
    if( 0 < user_number ):
        return True
    else:
        print("The number you have entered is not a positive number")
        return False

def getValidValue():
    while(True):
        usernumber = input("Please pick a positive number: ")
        if(checkIfNumber(usernumber)):
            usernumber = int(usernumber)
            if(checkIfpositive(usernumber)):
                return usernumber


def main():
    a = 0
    b = 1
    c = 0
    sumo = 0
    usernumber = getValidValue
    while(b < usernumber):
        sumo = sumo + b
        c = b
        b = b + a
        a = c
    print("The sum of all Fibonacci numbers smaller than", usernumber,"is", sumo, ".")   

main()
