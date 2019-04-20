from turtle import*
shape("turtle")

items=['red','blue','green']
for i in range(0,len(items)):
    color(items[i])
    begin_fill()
    forward(100)
    end_fill()

mainloop()