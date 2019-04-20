items=['chó', 'gà', 'mèo', 'hổ']
print(*items, sep=',')
i=int(input("nhập phần tử muốn loại bỏ: "))
items.pop(i)
print(*items, sep=',')