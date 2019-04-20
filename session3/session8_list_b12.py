items=['chó', 'gà', 'bò', 'hổ']
print(*items, sep=',')
a=0
b=len(items)
for i in range(0,b) :
    if items[i]=="LOL":
        items.pop(i)
    else: a=a+1 
if a==b:
    print("Phần tử này không tồn tại, kiểm tra lại")
else: print(*items, sep=',')

