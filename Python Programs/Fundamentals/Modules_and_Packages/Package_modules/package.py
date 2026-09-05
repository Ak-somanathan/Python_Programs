# Package modules
from Modules import calc
print(calc.mul(2,2))

# Locating a module
import sys
for i in sys.path:
    print(i)