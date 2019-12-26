no1=int(input("Enter the number"))
no2=int(input("Enter the number"))

try:
    res=no1/no2
    print("res",res)
except:
    no2=int(input("Enter value for no2"))
    print("exception occured")
    res=no1/no2
    print("res",res)
    try:
        res=no1/no2
        print("res=",res)
print("I have one database connection")