
def main():
    N = int(input("Please insert the width of the rectangle"))
    M = int(input("Please insert the height of the rectangle"))
    
    currrow = 0
    while (currrow < M):
        if(currrow == 0 or currrow == (M-1)):
            print(N * "*", end="\n")
        else:
            currcol = 0
            while(currcol < N):
                if(currcol == 0 or currcol == (N-1)):
                    print("*", end="")
                else:
                    print(" ", end="")

                currcol += 1
            print("", end="\n")
                

        currrow += 1

main()
