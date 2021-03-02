
a = int(input("choose"))
b = 1
e = 0
while(b < a//2):
    b = b + 1
    if(a % b == 0):
        e = 1
        break

if(e == 1):
    print("not prime")
else:
    print("prime")

