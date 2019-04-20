from turtle import*
a=int(input("Nhập vào 1 số: "))
shape("turtle")
for i in range(a):
    forward(100)
    right(360/a)

mainloop()