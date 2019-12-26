num = int(input("Enter the number"))
res=0

while(num!=0):
    digit=num%10
    res=res+(digit*digit*digit)

    num=num//10



#

print(res)
if(res == num):
    print("It is an amstrong number")
else:
    print("It is not an amstrong number")