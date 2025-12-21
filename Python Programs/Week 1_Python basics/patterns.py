#pattern-1
n=int(input("Enter a no: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#pattern-2
n=int(input("Enter a no: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

#pattern-3
n=int(input("Enter a no: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#pattern-4
n=int(input("Enter a no: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()

#pattern-5
n=int(input("Enter a no: "))
space=n-1
for i in range(0,n):
    for j in range(0, space):
        print(end=" ")
    space=space-1
    for k in range(0, i+1):
        print("*", end=" ")
    print()

#pattern-6
n=int(input("Enter a no: "))
for i in range(0,n):
    for j in range(0, i+1):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()


#pattern-7
n=int(input("Enter a no: "))
alp=65
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(alp),end=" ")
        alp+=1
    print()

#pattern-8
n=int(input("Enter a no: "))
for i in range(0,n):
    alp=65
    for j in range(0,i+1):
        print(chr(alp),end=" ")
        alp+=1
    print()

#pattern-9
n=int(input("Enter a no: "))
for i in range(0,n):
    a,b=1,0
    for j in range(0,i+1):
        print(a, end=" ")
        a,b=b,a
    print()

#pattern-10
n=int(input("Enter a no: "))
space=n-1
for i in range(0,n):
    for j in range(0,space):
        print(" ",end="  ")
    space=space-1
    for k in range(0,i+1):
        print("*",end=" ")
    print()
        




