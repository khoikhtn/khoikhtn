from random import randint
a=randint(0,100)
print(a)
if a < 30:
    print("Rainy")
elif a>=30 and a<60:
    print("Cloudy")
else: print("Sunny")