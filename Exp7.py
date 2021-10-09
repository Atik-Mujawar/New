class Parent:
    def show(self):
        print("In Parent Class")
    def inherit(self):
        print("Inherit from parent class")
class Child(Parent):
    def show(self):
        print("In Child Class")
    def greet(self, name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")
obj=Child()
print("----Inheritance----")
obj.inherit()
print("----Method Overiding----")
obj.show()
print("----Method Overloading----")
obj.greet()
obj.greet(" Atik")