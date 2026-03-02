# Inheritance(single inheritance)- used to inherit the properties and behaviors of one class into another

class parent:
    def sing(self):
        print("can sing")
class child(parent):
    def dance(self):
        print("can dance")

obj=child()
obj.dance()
obj.sing()

# Multiple inheritance - a class can be created based on more than one parent classes

class maths:
    def math_mark(self,m):
        self.m=m
        print(f"Maths score:{self.m}")
class science:
    def sci_mark(self,s):
        self.s=s
        print(f"Science score:{self.s}")
class total(maths,science):
    def tot_mark(self):
        print(f"Total score:{self.m+self.s}")

obj2=total()
obj2.math_mark(58)
obj2.sci_mark(32)
obj2.tot_mark()

# Multi-level inheritance - a class derived from another derived class

class school:
    def high_school_diploma(self):
        print("Finished HSC")
class college(school):
    def clg_graduate(self):
        print("Degree Holder")
class emp(college):
    def worker(self):
        print("Employee")

obj3=emp()
obj3.worker()
obj3.clg_graduate()
obj3.high_school_diploma()

# Hierarchical inheritance - contains multiple derived classes that are inherited from a single base class.

class parent:
    def __init__(self,networth):
        self.networth=networth
class child1(parent):
    def chd1(self):
        print(f"child1: {self.networth/3}")
class child2(parent):
    def chd2(self):
        print(f"child2: {self.networth/2}")

obj4=child1(1000)
obj4.chd1()
obj5=child2(4000)
obj5.chd2()

# Hybrid inheritance - combination of two or more types of inheritance is called as Hybrid Inheritance

class principal:
    def prin_method(self):
        print("Im the principal")
class hod(principal):
    def hod_method(self):
        print("Im the hod")
class it_hod(hod):
    def it_method(self):
        print("Im the it hod")
class cse_hod(hod,principal):
    def cse_method(self):
        print("Im the cse hod")

obj6=cse_hod()
obj6.cse_method()
obj6.hod_method()
obj6.prin_method()

