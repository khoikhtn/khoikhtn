items=['3','4','12','-1','99']
a=int(input("Enter a number: "))
b=0
for i in range(0,len(items)):
    if a==int(items[i]):
        b=1
        print("Found, position ",i)
        break
if b==0:
    print("Not found in our list")