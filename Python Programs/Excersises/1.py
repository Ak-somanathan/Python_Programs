#Problem 1

'''Input:
An integer units representing electricity consumption.

Process:

If units ≤ 100 → cost = units × 1

If 101–200 → cost = units × 2

If units > 200 → cost = units × 5

Output:
Print the electricity bill amount.'''

# Solution

units=int(input())
if units <= 100:
    cost=units*1
elif units>=101 and units<=200:
    cost=units*2
else:
    cost=units*5
print(cost)
