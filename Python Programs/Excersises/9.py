# Problem 1

'''Input:
A string correct_password.

Process:
Allow the user to enter password up to 3 attempts.

If entered password matches → stop checking

Else continue until attempts exhausted

Output:
Print "Login Successful" or "Account Locked".'''

# Solution

crt_pswd="Ak@123"
for i in range(3,0,-1):
    pswd=input("Enter your pswd: ")
    if crt_pswd==pswd:
        print("Successfully logged in")
        break
    else:
        print(f"Oops! wrong. you've {i-1} chances")
        if i==1:
            print("Account locked")
        continue

