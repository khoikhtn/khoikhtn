from random import randint
a=input("Nhập vào 1 từ: ")
items=list(a)
c=len(items)
for i in range (0,c) :
    d=randint(0,c-1)
    print(items[d].upper())
    items.pop(d)
    c=len(items)

