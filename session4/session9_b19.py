items=[48,50,55]
for i,item in enumerate(items):
    print(i,".",item)
a=int(input("Enter your new score: "))
items.append(a)
for i,item in enumerate(items):
    print(i,".",item)