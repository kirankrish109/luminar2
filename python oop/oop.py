class Person:
    def setVal(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name",self.name)
        print("age",self.age)
ob=Person()
ob1=Person()
ob.setVal("ajay",26)
ob.display()
ob1.setVal("kiran",23)
ob1.display()


