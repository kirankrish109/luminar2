num = int(input("Enter the number"))
flag = 0
i = 2
while(i<num):
    if(num%i==0):
        flag=flag+1
        print(num)
        break
    else:
        flag=0
    i+=1
if(flag==0):
    print("The number is prime")
else:
    print("The number is not prime")