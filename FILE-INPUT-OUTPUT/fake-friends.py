import operator



f=open("/home/kiran/Downloads/python files/fakefriends.csv","r")

dict={}

for temp in f:
    temp=temp.rstrip()
    data=temp.split(",")
    sn=data[0]
    name=data[1]
    age=data[2]
    numOffrnds=data[3]

    # print(name,age)
    if(age not in dict):
        # dict[age]=age
        dict[age]=1
    else:
        dict[age]+=1

# print(dict)
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))
print(sorted_dict[0])
