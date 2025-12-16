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


    
