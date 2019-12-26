flag=0
nlst=[]
lst=[]
# len=int(input("Enter the number"))
# for i in range(0,len):
#     num = int(input("Enter the element:"))
#     lst.append(num)
while (flag<3):
         lst=[2,3,4]
         lst.pop(flag)
         mul=lst[0]*lst[1]
         nlst.append(mul)
         flag=flag+1
print(nlst)