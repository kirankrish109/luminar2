num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

if(num1>num2):
    if(num1>num3):
        print(num1,"is greater")
    else:
        print(num3,"is greater")
elif(num1>num3):
    if(num1>num2):
        print(num1,"is greater")
    else:
        print(num2,"is greater")
elif(num1<num3):
        print(num3, "is greater")
else:
    print("all are equal number")