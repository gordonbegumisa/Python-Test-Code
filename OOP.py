class Dog:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def bark(cls):
        print("Woof!"), cls
        return

d = Dog('Fido','girl')
print(d.name, d.sex)  # Call property/attribute
d.bark() # Call method
