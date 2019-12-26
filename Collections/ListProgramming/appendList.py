lst=[]
cnt = int(input("Enter the length"))
for i in range(0,cnt):
    element = int(input("Enter the element:"))
    lst.append(element)
print(lst)

LstOdd=[]
LstEve=[]

for item in lst:
    if(item%2!=0):
        LstOdd.append(item)
    else:
        LstEve.append(item)
print("The odd list is \n",LstOdd)
print("The even list is \n",LstEve)