class Student:
    schoolname="luminarTechnolab"

    def setVal(self,id,name):
        self.id=id
        self.name=name
    def printVal(self):
        print(self.id,"==",self.name,"==",Student.schoolname)

    @classmethod
    def setSchool(cls,name):
        cls.schoolname=name

    @staticmethod
    def greetings():
        print("welcome")
s=Student()
s.setVal(100,"noname")
s.printVal()
s.setSchool("luminar Techonolab Sol")
s.printVal()
Student.greetings()
