num=int(input())
while len(str(num))>=2:
    add=0
    while num>0:
        add+=num%10
        num=num//10
    num=add
print(add)
    
    

    
    
