num = int(input("Enter the number:"))
i=2
# if(num==2):
#     print("It is a prime number")
flag=0
if(num==2):
    print("It is a prime number")
while(i<num):
    if(num%i==0):
        flag=flag+1

        break
    else:
        flag=0
    i+=1

if(flag==0):
    print("it is a prime number")
else:
    print("it is not a prime number")