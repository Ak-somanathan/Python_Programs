#string creation
a=input()
print(a)

b="akshaya"
print(b)

c='a'
print(c)

d='''Multi-line str'''
print(d)

e="""Multi-line string
         Multi-line string
         Multi-line string
     """
print(e)

#accessing a string
print(a[10])
print(a[-4])

# string slicing
print(b[0:5:2])
print(b[:5])
print(b[::2])
print(b[::-1])

# string iteration
for i in a:
    print(i, end=" ")

# string immutability
a="akshaya"
a="A"+a[1:]
print(a)

# deleting a string
del a

# updating a string
s="string"
m=s.replace("string","sting")
print(m)














