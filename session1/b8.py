from turtle import*
shape("turtle")
for i in [3,4,5]:
    for j in range(i):
        forward(100)
        left(360/i)

mainloop()