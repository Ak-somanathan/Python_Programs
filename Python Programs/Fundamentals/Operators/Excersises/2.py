#Problem 2

'''Input:
An integer basic_salary.

Process:
Calculate:

HRA = 20% of basic salary

DA = 15% of basic salary

PF = 8% of basic salary

Net salary = basic + HRA + DA − PF

Output:
Print the net salary.'''

# Solution

basic_salary=int(input())
hra=(20/100) * basic_salary
da=(15/100) * basic_salary
pf=(8/100) * basic_salary
net_salary=round(basic_salary + hra + da - pf)
print(net_salary)
