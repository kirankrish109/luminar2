f = open('/home/kiran/PycharmProjects/luminar_project/FILE-INPUT-OUTPUT/sampfile','r')
lst=[]
for data in f:

        lst.append(data.rstrip("\n"))

print(lst)

print("The even numbers are:")
for i in lst:
    num=int(i)
    if (num%2==0):
        print(num,end="\t")
