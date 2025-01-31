d = int(input("Enter Degree 1 if B.E. or 2 if M.E: "))
e = int(input("Enter 1 if experience is <5 year or 2 if >=5 year: "))

if d==1:
    if e==1:
        print("Salary is 30000")
    elif e==2:
        print("Salary 40000")
    else:
        print("Enter valid values")
elif d==2:
    if e==1:
        print("Salary is 50000")
    elif e==2:
        print("Salary 60000")
    else:
        print("Enter valid values")
else:
    print("Enter valid values")