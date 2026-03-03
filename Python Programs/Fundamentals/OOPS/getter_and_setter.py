# getter and setter -  methods used to access and update the attributes of a class.
class age:
    def __init__(self):
        self.__age=None

    # setter method
    def set_age(self,n):
        if n>18:
            self.__age=n
        else:
            print("Your age isn't valid")
 
    #getter method
    def get_age(self):
        if self.__age is None:
            return "Your age should be above 18"
        return self.__age

obj=age()
obj.set_age(25)
print(obj.get_age())


# proper example

class person:
    def __init__(self):
        self.__age=None
 
    @property
    def age(self):
        if self.__age is None:
            return "Your age should be above 18"
        return self.__age
    
    @age.setter
    def age(self,n):
        if n>18:
            self.__age=n
        else:
            print("Your age isn't valid")

obj=person()
obj.age=25
print(obj.age)


