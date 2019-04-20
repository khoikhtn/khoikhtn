a=input("Nhập các số cách nhau bởi dấu cách: ")
items=a.split(" ")
b=0
for i in range(0,len(items)):
    b=b+int(items[i])
print(b)
