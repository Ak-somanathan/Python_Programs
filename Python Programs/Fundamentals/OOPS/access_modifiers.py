class emp:
    def __init__(self, name, emp_id, role):
        self.name=name               # public
        self.__emp_id = emp_id    # private
        self._role = role                # protected
    def show_emp(self):
        print(f"Name: {self.name}\nId: {self.__emp_id} \nRole: {self._role}")

e1=emp("Akshaya",1,"Pm")
e1.show_emp()
print(e1.name)
print(e1._role)
print(e1.__emp_id)
