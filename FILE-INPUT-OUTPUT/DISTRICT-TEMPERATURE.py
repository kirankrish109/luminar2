df=open("Dict-temp","r")


dict={}

for temp in df:

    temp=temp.rstrip("\n")
    data=temp.split(",")
    district=data[0]
    tem = data[1]
    # print("temp",tem)
    # print("district",district)
    if(district not in dict):
        dict[district]=tem

    else:
        old=dict[district]
        if(old<tem):
            dict[district]=tem
        else:
            dict[district]=old
print(dict)


