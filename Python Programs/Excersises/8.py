# Problem 2

'''Input:
A string product_name, a float price, and an integer quantity.

Process:
Calculate total amount = price × quantity.

Output:
Print the product name and total amount.'''

# Solution

product_name = input()
price = float(input())
qty = int(input())
amt = round(price * qty)
print(amt)
