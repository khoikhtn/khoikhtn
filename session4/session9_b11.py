a=input("Nhập 1 danh sách các số cách nhau bởi dấu phẩy: ")
b=a.split(",")
for i in range(0,len(b)):
    if int(b[i])%2==0:
        print(b[i])