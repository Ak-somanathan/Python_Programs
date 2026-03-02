# Encapsulation - Hiding internal details of a class using access modifiers.
# without encapsulation
class emp:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

obj=emp("Akshaya",101,20000)
print(obj.salary)

# With encapsulation
class emp:
    def __init__(self,name,id,salary):
        self.name=name
        self._id=id                        # protected var
        self.__salary=salary          # private var
    def details(self):
        print(self.name)
        print(self._id)
        print(self.__salary)
        
obj1=emp("Akshaya",101,20000)
obj1.details()
print(obj1.__salary)
print(obj1._emp__salary)           # to access private var outside the class



