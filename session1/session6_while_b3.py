a=input("Nhập mk: ")
while True:
    if a.isalpha():
        a=input("nhap lại mk: ")
    elif len(a)<8:
        a=input("nhap lại mk: ")
    else: 
        print("OK")
        break