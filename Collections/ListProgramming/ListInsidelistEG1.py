lst=[[10,"ABC",1500],
     [11,"CDE",20000],
     [12,"FGH",25000],
     [13,"IJK",30000]]
flag=0
sum=0
for item in lst:
    if(item[2]>20000):
        print(item)
        sum=sum+item[2]
        flag+=1
print("The are ",flag,"employees\n And their salary sum is:",sum)