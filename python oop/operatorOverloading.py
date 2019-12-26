class Book:
    def __init__(self,pages):
        self.pages=pages


    def __mul__(self, other):
        return Book(self.pages*other.pages)

    def __truediv__(self, other):
        return Book(self.pages/other.pages)



    def __str__(self):
        return str(self.pages)

b1=Book(100)
b2=Book(200)
b3=Book(400)
print(b1*b2*b3)
print("The div is", b3/b2)
