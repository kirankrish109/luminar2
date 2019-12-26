print("team,match,win,lost,points")
isl=[["ATK",5,3,1,10],["bengluru_fc",5,2,0,9],["goa",4,2,0,8],["northeastuntd",4,2,0,8],["jamshedpur",4,2,1,7],
     ["odisha",5,1,2,5],["kerala_blasters",5,1,3,4],["mumbai",4,1,2,4],["chennai",5,1,3,4],["hydrabad",5,1,4,3]]
cup=[]
for i in isl:
    cup.append(i[4])
    if(i[1]>4):
        print("teams played more than 4 matches",i[0])
    if(i[2]>2):
        print("teams won more than 2 matches",i[0])
    if (i[3]>2):
        print("the team lost mor than 2 matches", i[0])
print("cup winner max points",max(cup))

