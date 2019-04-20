items=['150300','247100','333300','266800','420900','318000']
maxx=1
for i in range(0,len(items)):
    if int(items[i])>=maxx:
        maxx=int(items[i])
minn=10000000
for j in range(0,len(items)):
    if int(items[i])<=minn:
        minn=int(items[i])
print("max=",maxx)
print("min=",minn)
