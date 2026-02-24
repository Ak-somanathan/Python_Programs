# dictionary creation
info={1:"akshaya", "age":"21", "loc":"pondicherry"}
print(info)

info2=dict(name="somanathan", age="60")
print(info2)

emp=dict()

# accessing dictionary
print(info[1])
print(info2.get("name"))

# adding and updating
info["initial"]="V"
print(info)

info[1]="ak"
print(info)

# deleting
del emp

del info2["age"]
print(info2)

d=info.pop("age")
print(d)

k,v=info.popitem()
print(k,v)

c=info2.clear()
print(info2)

# iterating
for i in info.values():
    print(i)

for i in info.keys():
    print(i)

for i,j in info.items():
    print(i,j)

# nested dictionary
info3={1:"student", 2:{"name":"somanathan", "age":"60"}}
print(info3[2])
