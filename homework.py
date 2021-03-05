
def checkIfNumber(user_number):
    if(user_number.isnumeric()):
        return True
    else:
        print("The number that you have entered is not a valid number.")
        return False


def getValidValue():
    while(True):
        usernumber = input("Please pick a positive number: ")
        if(checkIfNumber(usernumber)):
            usernumber = int(usernumber)
            return usernumber


def DecimalToBinary(user_number):	
	if (user_number > 1):
		DecimalToBinary(user_number // 2)
	print(user_number % 2, end = '')

def main():
    a = 0
    b = 1
    c = 0
    sumo = 0
    d = 1
    e = 0
    usernumber = getValidValue()
    
    
    while(b < usernumber):
        sumo = sumo + b
        c = b
        b = b + a
        a = c
    print("The sum of all Fibonacci numbers smaller than", usernumber,"is", sumo, ".")

    
    
    
    if(usernumber == 1 or usernumber == 0):
        print(usernumber, "is neither prime nor composite")
    else:
        while(d < usernumber//2):
            d = d + 1
            if(usernumber % d == 0):
                e = 1
                break
        if(e == 1):
            print(usernumber, "is not a prime number")
        else:
            print(usernumber, "is a prime number")
    
    
    print("The binary representation of", usernumber, "is ", end = '')
    DecimalToBinary(usernumber)
    print("\n")


        
main()
