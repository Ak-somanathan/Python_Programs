#Problem 2

'''Input:
A string name and three integers m1, m2, m3.

Process:
Calculate total and average marks.

Output:
Print:

total marks

average marks (integer value)'''

# Solution

name=input()
m1,m2,m3=map(int,input().split())
total_marks=m1+m2+m3
avg_marks=int(total_marks/3)
print(total_marks, avg_marks,sep="\n")
