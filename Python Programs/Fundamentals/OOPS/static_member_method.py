# static member - class variable which belong to the class itself, rather than to any specific object.

class add:
    c=4
    def __init__(self, a, b):
        self.a=a
        self.b=b
        c=20
        print(self.a+self.b+c)
obj=add(10,5)
print(add.c)

# static method - method that belongs to the class, not to the any object

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # Instance method
    def sub(self):
        return self.a - self.b
    
    # Static method
    @staticmethod
    def add(a, b):
        return a + b

obj = Calc(20, 10)
print("Subtraction:", obj.sub())
print("Addition:", Calc.add(5, 3))














