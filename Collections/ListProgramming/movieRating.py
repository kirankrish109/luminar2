movie=[[1,"half girlfriend",4,1991],[2,"mission impossible",5,1991],[3,"batman",4.5,1991]]
flag=0
for item in movie:
    if(item[2]>4.5):
        print(item[1], "is the movie have rating greater than 4.5")
    if(item[3]==1991):
        flag=flag+1
        print(item,"is the movie released in 1991 and total count is :",flag)
