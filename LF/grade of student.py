mark1 = float(input("Enter the mark1"))
mark2 = float(input("Enter the mark2"))
mark3 = float(input("Enter the mark3"))

total = (mark1+mark2+mark3)
if(total>140):
    print("The grade is A+")
elif(total>130 and total <140):
    print("The grade is A")
elif(total>120 and total <130):
    print("The grade is B+")
elif(total>110 and total <120):
    print("The grade is B")

elif(total>100 and total<110):
    print("The grade is c")
else:
    print("The student failed")