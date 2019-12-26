num = int(input("Enter the number for search:"))
flag=0
lst=[1,2,3,4,5]
for item in lst:
    if(item==num):
        print(item)
        flag=flag+1
        break
    else:
        flag=0

if(flag==0):
    print("NotFound")
else:
    print("Found")