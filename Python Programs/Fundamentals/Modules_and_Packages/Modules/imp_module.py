# importing a module which is user def
import calc
print(calc.div(20,55))

# Types of Import statements
# 1. Import from module

from math import factorial,sqrt
print(sqrt(16))
print(factorial(6))

# 2. Import all names
from math import *
print(floor(15.4865))

# 3. Import with alias
import math as m 
print(m.log(20))

# Types of modules
# 1. Built-in modules
import random
print(random.randint(45,46))

# 2. User-def modules
import calc
print(calc.sub(20,55))

# 3. External or third-party modules
import requests
r=requests.get("https://www.geeksforgeeks.org/python/python-modules/")
print(r.status_code)
