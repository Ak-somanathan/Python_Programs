# constructor - a special method automatically called when a object of a class is created

class sample:
    def __init__(self,n):
        self.n=n
    def func1(self):
        return self.n
obj=sample(12)
print(obj.func1())

# default constructor

class bike:
    def __init__(self):
        self.name="LML"
        self.yr=1990
obj1=bike()
print(obj1.name, obj1.yr)

# parameterized constructor

class car:
    def __init__(self,name,yr):
        self.name=name
        self.yr=yr
        print(self.name, " - ", self.yr)
obj2=car("Ferrari 125 S", 1947)
