class student:
    def setVal(self,name,id,school,mark):
        self.name=name
        self.id=id
        self.school=school
        self.mark=mark

    def display(self):
        print("name",self.name)
        print("id",self.id)
        print("schoo:",self.school)
        print("mark:",self.mark)
    def __str__  (self):
        return self.name
lst=[]

st1=student()

st1.setVal("kiran",19,"mmhs",91)
# st1.display()
# st2.setVal("arun",25,"mmhs",50)
# st2.display()

lst.append(st1)
# lst.append(st2)
for ob in lst:
    print(ob)
