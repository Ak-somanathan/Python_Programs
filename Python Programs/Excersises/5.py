# Problem 1

'''Input:
A single value x.

Process:
Determine whether x is:

Integer

Float

String

Output:
Print the data type.'''

# Solution

x = input()
try:
    int(x)
    print("Integer")
except:
    try:
        float(x)
        print("Float")
    except:
        print("String")
