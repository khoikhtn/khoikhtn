from random import randint, choice
points=0

while True:
    a=randint(0,10)
    b=randint(0,10)
    op=choice(['+','-','*','/'])
    kqdung = 0
    if op=='+':
        kqdung = a + b
    elif op == '-':
        kqdung = a - b
    elif op=='*':
        kqdung = a * b
    elif op=='/':
       kqdung = a / b

    erro = randint(-1,1)
    ketqua = kqdung + erro
    print(a,op,b,"=",ketqua)
    c=input("Điền Đúng hoặc Sai: ")
    if ketqua==kqdung:
        if "Sai" in c or "sai" in c:
            print("Game over")
            print(points, "điểm")
            break
        elif "Đúng" in c:
            points += 1
    else:
        if "Đúng" in c or "đúng" in c:
            print("Game over")
            print(points, "điểm")
            break
        elif "Sai" in c:
            points += 1





