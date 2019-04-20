n=int(input("Nhập vào 1 số: "))
if(n%2==1):
    for i in range(n,2,-2):
        print(i)
else:
    for i in range(n-1,0,-2):
        print(i)