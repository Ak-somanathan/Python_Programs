# Problem 2

'''Input:
A string password.

Process:
Create a function to check:

password length ≥ 8

password contains at least one digit

Output:
Print "Strong" or "Weak".'''

# Solution

p=input()
def pswdchecker(pswd):
    if any(i.isdigit() for i in pswd) and len(pswd)>=8:
        print("Strong pswd")
    else:
        print("Week pswd")
pswdchecker(p)
