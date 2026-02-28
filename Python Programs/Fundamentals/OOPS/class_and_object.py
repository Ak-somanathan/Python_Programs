# class - blueprint that contains attributes of a particular objects and its all the functions.

class student:
    def __init__(self, name):
        self.name=name
        
    def fname(self):
        print(f"My name is {self.name}")

# object - instance of a class.
std_obj = student("Akshaya")
std_obj.fname()
std_obj.age=21
print(f"Age: {std_obj.age}")

# simple example

class Simple_calculation:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self): return self.a+self.b
    def sub(self): return self.a-self.b
    def mul(self): return self.a*self.b
    def div(self): return self.a/self.b

obj_cal = Simple_calculation(5,10)
print(obj_cal.add())
print(obj_cal.sub())
print(obj_cal.mul())
print(obj_cal.div())

