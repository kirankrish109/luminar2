class Parent:
    def phone(self):
        print("i have nokia 1155")
class Child(Parent):
    def phone(self):
        print("i have one plus 7")

c = Child()
c.phone()