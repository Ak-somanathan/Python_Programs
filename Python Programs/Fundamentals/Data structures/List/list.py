#List - mutable, ordered and index-based

#list creation
a=[1,0,-5]
b=['a','akshaya','6451']
c=[True, False]
d=[1,["akshaya","18"],3]
print(a,b,c,d)

#using list()
a=list((1,2,'3',4))
b=list("akshaya")
print(a,b)

#with repeated elements
a=[2]*5
print(a)

#accessing elements
print(a[2])
print(b[0:3])

#adding elements
a.append(3)
b.extend(["kumar","dhanam"])
c.insert(2,True)
d.clear()
print(a,b,c,d)

#updating elements
a[1]=20
print(a)

#removing elements
a=[1,2,3,4,5]
a.remove(5)
print(a)
a.pop(1)
print(a)
del a[2]
print(a)

#iterating list
info=["my","name","is","akshaya"]
for i in info:
    print(i,end=" ")

#nested list
matrix=[ [10,5,0],
               [74,1,-9],
               [8,92,37] ]
print()
print(matrix[1][0])

#list comprehension
n=[i for i in range(0,10)]
print(n)







