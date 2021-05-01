

def drawwithwhile(N, M):
    print("Printing with for loop")

   
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
        drawwithfor(N, M)

def drawwithfor(W, H):
    print("Printing with for loop")
    for(currrow == 1 or currrow == H):
        print(W * "*")
    else: 
        for(currcol


def main():
    N = int(input("Please insert the width of the rectangle: "))
    M = int(input("Please insert the height of the rectangle: "))
    drawwithwhile(N, M)
    drawwithfor(N, M)
main()
