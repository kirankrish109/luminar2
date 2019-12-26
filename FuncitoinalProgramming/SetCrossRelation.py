lst1=[1,2,3]
lst2=[4,5,6]
lst=[]

for i in lst1:
    for j in lst2:
         lst3 = (i,j)
         lst.append(lst3)

print(lst)
