n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("{} is a perfect num".format(n))
else:
    print("{} is not a perfect num".format(n))
