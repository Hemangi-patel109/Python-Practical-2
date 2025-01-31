a = int(input("ax^2 + bx + c \nEnter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b*b - 4*a*c

if d>0:
    print("Root are real.\n")
    print("Root1: ",(-b+d**0.5)/2*a,"\tRoot2: ",(-b-d**0.5)/2*a)
elif d==0:
    print("Roots are equal: ",(-b/2*a))
else:
    print("No Root")