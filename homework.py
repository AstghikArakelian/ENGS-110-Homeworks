import math
usernumber = input("Please instert a positive number - ")

def checkIfNumber(usernumber):
    if(usernumber.isnumeric()):
        return True
    else:
        print("The number that you have entered is not a valid number.")
        return False

def checkIfpositive(usernumber):
    if( 0 < usernumber ):
        return True
    else:
        print("The number you have entered is not a positive number")
        return False

def main
firstnum = 0
secondnum = 1
sum = 0
a = 1
while(True):
    while(secondnum < usernumber):
        sum = firstnum + secondnum
        secondnum = secondnum + firstnum
    else:
        print("The sum of all Fibonacci numbers smaller than", usernumber, "is", sum,".")
    while(a < math.sqrt(usernumber)):
        if(usernumber % a == 0):
            a = a + 1
        else:
           print("The number", usernumber, "is not a prime number")
    else:
        print("The number", usernumber, "is a prime number")


