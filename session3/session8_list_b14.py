items=['chó', 'gà', 'mèo', 'chuột']
print(*items, sep=',')
a=input("Nhập tên phần tử muốn loại bỏ: ")
items.remove(a)
print(*items, sep=',')