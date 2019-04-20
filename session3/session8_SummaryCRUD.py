items=['chó', 'mèo', 'gà', 'hươu', 'lợn']
while True:
    chon=input("Chọn C,R,U hay D: ")
    if 'c' in chon or 'C' in chon:
        a=input("Nhập thứ bạn thích: ")
        items.append(a)
        print(*items, sep=',')
    elif 'r' in chon or 'R' in chon:
        if len(items)==0:
            print("Danh sách rỗng")
        else:
            for item in items:
                print(item)
    elif 'u' in chon or 'U' in chon:
        b=int(input("Nhập phần tử muốn thay đổi: "))
        c=input("Nhập thứ muốn thay đổi: ")
        items[b]=c
        print(*items, sep=',')     
    elif 'd' in chon or 'D' in chon:
        d=int(input("Bạn muốn xóa vị trí nào: "))
        items.pop(d)
        print(*items,sep=',')
