#opening a file
file=open(r"C:\Users\LENOVO\OneDrive\Documents\Python\Fundamentals\File Handling\sample_file.txt","r")
print(file)

file1=open(r"C:\Users\LENOVO\OneDrive\Documents\Python\Fundamentals\File Handling\sample_file.txt","w")
print(file1)

file2=open(r"C:\Users\LENOVO\OneDrive\Documents\Python\Fundamentals\File Handling\sample_file.txt","a")
print(file2)

#checking file properties
print("File name:", file.name)
print("Mode:", file.mode)
print("Is Closed ? ", file.closed)

#reading a file
content=file.read()
print(content)

#writing a file
with open(r"C:\Users\LENOVO\OneDrive\Documents\Python\Fundamentals\File Handling\sample_file.txt","w") as file:
    file.write("Name: Akshaya somanathan\n")
    file.write("Age: 21")

#closing a file
file.close()

#handling exceptions when closing a file
try:
    file = open(r"C:\Users\LENOVO\OneDrive\Documents\Python\Fundamentals\File Handling\sample_file.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()














