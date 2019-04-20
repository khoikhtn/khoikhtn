items=['red','green','blue']
print(*items,sep=',')
a=input("Nhập một màu: ")
items.append(a)
print(*items,sep=',')