#Problem 1

''' Input:
An integer price and an integer quantity.

Process:
Calculate:

total cost = price × quantity

GST = 18% of total cost

final amount = total cost + GST

Output:
Print the total cost, GST, and final amount each on a new line.'''

# Solution
price, quantity = map(int, input().split())
total_cost=price*quantity
gst=round((18/100) * total_cost)
bill_amt=total_cost+gst
print(total_cost, gst, bill_amt, sep="\n")
