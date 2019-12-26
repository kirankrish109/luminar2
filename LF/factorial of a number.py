num = int(input("Enter the number"))
i=1
fact=1

while(i<=num):
    fact=fact*i
    if(i==num):
        print(fact)

    i+=1

