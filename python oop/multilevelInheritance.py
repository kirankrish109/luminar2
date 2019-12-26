class A:
    def m(self):
        print("inside A")
class B(A):
    def m1(self):
        print("inside b")
class C(B):
    def m2(self):
        print("inside C")

c=C()
c.m()
c.m1()
c.m2()
