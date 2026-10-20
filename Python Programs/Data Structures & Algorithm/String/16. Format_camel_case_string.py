s = input()
res = ""

for i in s:
    if i.isupper() and res:
        res += " "
    res += i.lower()
        
print(res)