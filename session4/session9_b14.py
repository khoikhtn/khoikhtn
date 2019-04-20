items1=['ST','BĐ','BTL','CG','ĐĐ','HBT']
items2=['150300','247100','333300','266800','420900','318000']
maxx=-1
for i in range(0,len(items2)):
    if int(items2[i])>=maxx:
        maxx=int(items2[i])
        ten1=items1[i]
minn=10000000
for j in range(0,len(items2)):
    if int(items2[i])<=minn:
        minn=int(items2[i])
        ten2=items1[j]
print("max:",ten1)
print("min:",ten2)
