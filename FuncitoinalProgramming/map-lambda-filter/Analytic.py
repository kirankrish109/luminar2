class Student:
    def __init__(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total

    def __str__(self):
        return self.name
f = open("/home/kiran/PycharmProjects/luminar_project/FuncitoinalProgramming/map-lambda-filter/sampleFileAnalytics","r")

StudentList=[]
lst=[]
for lines in f:
    lst=(lines.rstrip("\n").split(","))
    print(lst)
    id=lst[0]
    name=lst[1]
    total=lst[2]
    StudentList.append(Student(id,name,total))
mlist = list(filter(lambda o:int(o.total)>170,StudentList))

for ob in mlist:
    print(ob)
