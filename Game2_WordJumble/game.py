from random import randint
lists=['super', 'pirate', 'battle', 'hero', 'machine', 'ninja']
d=0
while True:
    a=randint(0,len(lists)-1)
    items=list(lists[a])
    for i in range (0,len(items)):
        b=randint(0,len(items)-1)
        print(items[b].upper())
        items.pop(b)
    c=input("Hãy sắp xếp lại thứ tự: ")
    if lists[a] in c:
        d=d+1
    else: 
        print("Game over")
        print(d,"điểm")
        d=0
        break
    



