items=['red','blue','green','yellow']
for i,item in enumerate(items):
    print(i,item)
a=input("Item to delete: ")
if a.isdigit():
    items.pop(int(a))
    print(*items,sep=',')
else:
    items.remove(a)
    print(*items,sep=',')