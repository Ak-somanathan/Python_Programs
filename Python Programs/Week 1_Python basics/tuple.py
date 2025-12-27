'''Tuple - immutable, ordered, heterogeneous'''

#tuple creation
a=()
n=(1,2,3,4)
t=tuple('akshay')
s=("akshaya",20)
l=list((1,2,3))
lt=tuple(l)
print(n,t, s, lt)

#accessing
print(n[2])
print(lt[0:2])

#concatenate
print(n+lt)
r=n+lt

#slicing
print(r[::2])
print(r[::-1])

#deleting
del a

#unpacking with asterik
a,b,*c,d=r
print(a,b,c,d)
