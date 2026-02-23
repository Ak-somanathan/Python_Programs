# Problem 2

'''Input:
An integer n followed by n integers.

Process:

Skip negative numbers

Stop processing if a number greater than 100 appears

Output:
Print only the valid numbers.'''

# Solution

n=int(input())
l=list(map(int, input().split()))
for i in l:
    if i<0 or i>100:
        continue
    else:
        print(i, end=" ")
