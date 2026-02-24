# array creation
import array as arr
a=arr.array('i',[1,2,3,4])
print(a)

# adding
a.insert(3,5)
print(a)
print(*a)

# accessing
print(a[3])

# removing
a.remove(5)
a.pop(0)

# slicing
print(*a[2:])

# searching
print(a.index(3))

# updating
a[0]=1
print(*a)






