# question:list = [2,3,4,7,9], if we give input as 6, 2 and 4 should be retuned

lst=[2,3,4,7,9]
slst=sorted(lst)
num = int(input("Enter the number"))
#method 1
# for item in lst:
#     for item2 in lst:
#         if((item+item2)==num):
#             print("(",item,item2,")")
#
#             break

low=slst[0]

up=len(slst)

while(low<up):
    if(lst[low]+lst[up]==num):
        print(slst[low],slst[up])
    else:
        up=up-1

