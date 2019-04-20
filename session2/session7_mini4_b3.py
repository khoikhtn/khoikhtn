a=input("Nhập tên đăng nhập: ")
b=input("Nhập mật khẩu: ")
while True:
    if b.isalpha() or b.isdigit():
        b=input("Nhập lại mật khẩu có số và chữ: ")
    else:
        if len(b)<=8:
            b=input("Nhập lại mật khẩu trên 8 chữ: ")
        else: break

c=input("Nhập lại mật khẩu: ")
while True:
    if b==c:
        d=input("Nhập email:")
        while True:
            if "@" in d and "." in d:
                print("Đăng kí thành công")
                break
            else: e=input("Nhập lại email: ")

    else: e=input(("Nhập lại mật khẩu:"))

