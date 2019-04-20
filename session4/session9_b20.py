items=[48,50,120,55,10,56,78]
maxx1=-1
maxx2=-1
for j in range(0,len(items)):
    for i in range(0,len(items)):
        if int(items[i])>=maxx1:
            maxx1=int(items[i])
            maxx2=i
    print(j+1,".",maxx1)
    items.pop(maxx2)
    maxx1=-1
    maxx2=-1
    
items=[48,50,120,55,10,56,78]
a=int(input("Nhập vào 1 số: "))
items.append(a)
maxx1=-1
maxx2=-1
for j in range(0,len(items)):
    for i in range(0,len(items)):
        if int(items[i])>=maxx1:
            maxx1=int(items[i])
            maxx2=i
    print(j+1,".",maxx1)
    items.pop(maxx2)
    maxx1=-1
    maxx2=-1