lst=[1,2,3,5,6]
ln = len(lst)
# for i in range(0,ln):
#     print(lst[i],end="\t")

for item in lst:
    if(item%2==0):
        print(item)