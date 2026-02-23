# Problem 1

'''Input:
Two integers balance and withdraw_amount.

Process:
Create a function that:

checks if withdraw_amount ≤ balance

returns remaining balance if valid

returns "Insufficient Balance" otherwise

Output:
Print the function return value.'''

# Solution

def balchecker(withdraw_amt, balance):
    if withdraw_amt <= balance:
        print(balance - withdraw_amt)
    else:
        print("Insufficient balance")
w=int(input())
b=int(input())
balchecker(w,b)
