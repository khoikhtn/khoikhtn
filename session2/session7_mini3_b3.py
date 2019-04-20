a=int(input("nhập vào tháng: "))
if a==2:
    print("28 ngày")
elif a%2==1 and a<8:
    print("31 ngày")
elif a%2==0 and a>7:
    print("31 ngày")
else: print("30 ngày")