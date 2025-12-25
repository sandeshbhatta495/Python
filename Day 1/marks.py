gpa_main=float(input("Enter the gpa:"))
if(gpa_main>0.0):
    print("you are passed.")
    gpa_obtained=float(input("Enter the gpa between(0.01-4)"))
    if(gpa_obtained>3.60):
        print("You obtained A+ grade.CONGRALAUTIONS!")
else:
    print("You have failed.")
