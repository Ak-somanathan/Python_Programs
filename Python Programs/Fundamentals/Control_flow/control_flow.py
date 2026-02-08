#conditional statements - If statement

a=int(input())
b=int(input())
if a>b:
    print(f"{a} is greater than {b}")

#if..else statement

age=int(input("Enter your age: "))
if age>18:
    print("Youre Major")
else:
    print("Youre not a Major")

#elif statement

if age>=1 and age<=14:
    print("child")
elif age>=15 and age<=20:
    print("Teen")
elif age>=20:
    print("Lady")
else:
    print("invalid age")

#nested if..else statement

age=int(input("Enter age "))
if age>0:
    if age>0 and age <=50:
        print("50% discount")
    else:
        if age >50 and age<=70:
            print("70% discount")
else:
    print("NO discount")

#match-case statement

gen=int(input())
match gen:
    case 0:
        print("Male")
    case 1:
        print("Female")
    case _:
        print("others")

#for loop
name=input()
print("My name is: ")
for i in name:
    print(i, sep="")

n=int(input("Enter a no:"))
for i in range(1,11):
    print(f"{i} * {n} = {i*n}")

print("Even nos btw 2 - 20 are: ")
for i in range(2,20,2):
    print(i, end=" ")
else:
    print()
    print("20 is not printed, cuz the range functions stops by -1. ie., if the stop value is 20, it stops in 19 itself")

#nested for loop
n="1234"
m="abcd"
for i in n:
    for j in m:
        print(j, end=" ")
    print()
    
#while loop
i=0
while i<=10:
    print(i, end=" ")
    i+=1

#nested while loop

n=0
m=int(input("what no. table you want? :"))
while n<10:
    n+=1
    while m:
        print(n*m)
        break

#continue statement

for i in range(1,11):
    if i==5:
        continue
    print(i)

#break statement
    
for i in range(1,11):
    if i==5:
        break
    print(i)


    

