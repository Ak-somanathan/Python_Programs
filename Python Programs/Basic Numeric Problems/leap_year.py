year=int(input())
if year%4==0 and (year%100!=0 or year%400==0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
