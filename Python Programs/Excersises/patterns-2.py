'''#pattern-1
n=int(input("Enter a no: "))
space=n-1
for i in range(n,0,-1):
    for j in range(space,0,-1):
        print(end=" ")
    space=space-1
    for k in range(i,0,-1):
        print("*",end=" ")
    print()'''

#pattern-2
n=int(input("Enter a no: "))
space=n-1
for i in range(0,n):
    for j in range(0, space):
        print(end=" ")
    space=space-1
    for k in range(0, i+1):
        print("*", end=" ")
    print()

#pattern-3
n=int(input("Enter a no: "))









