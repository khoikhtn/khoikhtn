items=["chó", "mèo", "bò", "gà"]
print(*items, sep=",")
i=int(input("Nhập phần tử muốn thay đổi: "))
items[i]=input("nhập thứ bạn thích: ")
print(*items, sep=",")