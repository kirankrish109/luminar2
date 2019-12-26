class Parent1:
    def m1(self):
        print("Inside p1")
class Parent2:
    def m1(self):
        print("Inside p2")
class child (Parent1,Parent2):
    def m3(self):
        print("inside m3")

c = child()
c.m3()
c.m1()
