# Polymorphism - a method taking different forms in different contexts.

# compile time - done by method overloading
class Human:
    def __init__(self,name):
        self.name=name
        print(f"Name: {self.name}")

    def age(self, n=None,birthyr=None, yr=None):
        if birthyr is not None and yr is not None:
            print(f"Age is {yr-birthyr}")
        else:
            print(f"Age is {n}")
obj=Human("Akshaya")
obj.age(17)
obj.age(birthyr=2005,yr=2026)

# Run-time -  done by method overriding
class parent:
    def name(self):
        return f"Initial: {a}"
    
class child(parent):
    def name(self):
        return f"Name: {a}"

obj=None
a=input()
if len(a)==1:
    obj=parent()
else:
    obj=child()
print(obj.name())
    
