import pyglet
from datetime import datetime, time

a=int(input("nhap gio: "))
b=int(input("nhap phut: "))
while True:
    if  datetime.now().hour==a and datetime.now().minute==b:
        # music=pyglet.resource.media('sample.wav')
        # music.play()
        # pyglet.app.run()
        print("Hello")
        break
    else: continue
