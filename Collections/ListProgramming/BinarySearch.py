lst=[]
cnt = int(input("Enter the length of list"))
for i in range(0,cnt):
    element = int(input("Enter the element:"))
    lst.append(element)
print("The list is :",lst)

Sortlst=sorted(lst)
print("Sorted list is ",Sortlst)
flag=0
low = lst[0]

up=len(Sortlst)
mid=(low+up)//2
item=int(input("Enter the number to search:"))
while(low<up):
    if (item > Sortlst[mid]):
        low=mid+1
    elif(item<Sortlst[mid]):
        up=mid-1
    elif(item==Sortlst[mid]):
        flag=flag+1
        break

    mid=(low+up)//2
if(flag>0):
    print("Element found")
else:
    print("Element Not Found")