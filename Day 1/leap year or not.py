year=int(input("Enter the Year:"))

if(year%4==0):
    print("Leap Year.")
     elif(year%100!=0):
         print("Leap year")  
elif year % 400 == 0 :
        print("Leap Year.")
    else:
    print("Not leap year")

else:
    print("Not Leap Year.")