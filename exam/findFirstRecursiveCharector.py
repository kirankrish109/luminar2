str="ABBAAB"










# lst=[num for i in str for j in str if i==j]
# print(lst)

for i in str:
    for j in str:
        if (i == j):
            print( i ,"is repeated")
            flag=1
            break
    if flag==1:
        break