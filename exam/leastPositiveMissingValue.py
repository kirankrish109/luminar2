lst=[-2,-5,-9,-1,0,1,3,4,5,6]


flag=0
    # if (lst[i]-lst[i+1]==1):
lst2 = [i for i in lst if i>0]
sorted(lst2)
print(lst2)
low = (min(lst2))

high=(max(lst2)+1)

for i in lst2:
    print(lst2[i])
    # if (lst2[i+1]-lst2[i]==1):
    #     flag=flag+1
    # else:
    #     print(lst[i]+1)





print(high)
print(low)




