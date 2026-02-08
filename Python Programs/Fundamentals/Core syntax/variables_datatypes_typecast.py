#variable

n=10
s="Akshaya"
b=True
f=1.6
c='c'
a=b=c=10
a,b,c,d = 10,-50,9.8,"Name"

#datatypes: int, string, float, boolean,...

n=int(input("Enter a Integer: "))
s=str(input("Enter string"))
b=bool(input("Enter boolean"))
f=float(input("Enter float"))

#input format

n=10
n=input("Enter a no: ")

#output format

print("Hello")
print(a)
print("My {} is Akshaya".format(d))
print(f'I am {n} years old.')

#typecasting - Implicit

f=2.0
div = n/f

#explicit

n=str(n)
print(type(n))

b=str(b)
print(type(b))

f=int(f)
print(type(f))

m=10
m = float(m)
print(type(m))

