items1=['117.43','9.224','43.35','12.04','9.96','10.09']
items2=['150300','247100','333300','266800','420900','318000']
b=0
for i in range(0,len(items1)):
    a=int(items2[i]) / float(items1[i])
    b=b+a

c=b/len(items1)
print("MĐDSTB=",c)