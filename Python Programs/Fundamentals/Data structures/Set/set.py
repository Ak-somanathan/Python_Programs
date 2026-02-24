# set creation
s={1,2,1,4,3}
m=set()
n=set("akshaya")
m1=set(["akshaya","somanathan"])
print(s,m,n,m1)

# adding
s.add(4)
print(s)

s.update([5,6,7])
print(s)

# removing
s.remove(7)
s.pop()
print(s)

m1.clear()
print(m1)

# frozen set
s2=frozenset(s)
print(s2)
