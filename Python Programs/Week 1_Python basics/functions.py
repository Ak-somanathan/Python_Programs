#functions
def function_name(parameter):
    print(parameter)
function_name("function-statement")

#functional arguments - default arguments
def add(a, b=10):
    print(a+b)
add(5)

#keyword arguments
def sub(a,b):
    return a-b
print(sub(b=5,a=15))

#positional arguments
def positional_arg(a,b):
    print(a,b)
positional_arg(5,10)

#arbitary arguments
def nkwdargs(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print(sum)
nkwdargs(10,58,2,3)

def kwdargs(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
kwdargs(name="Akshaya",yrs=20, rel="Friend")

#nested functions
def function1(a,b):
    print(f"{a}+ {b} = {a+b}")
    def function2(c):
        print(f"{a+b} + {c} = {a+b+c}")
    function2(50)
function1(20,16)

# without lambda function
n=int(input())
def cube(n): return n*n*n
print(cube(n))

#with lambda function
cube = lambda n: n*n*n
print(cube(n))
