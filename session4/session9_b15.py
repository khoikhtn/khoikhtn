items1=['117.43','9.224','43.35','12.04','9.96','10.09']
items2=['150300','247100','333300','266800','420900','318000']
for item in items1:
    print(item)
for i in range(0,len(items1)):
    print("Mật độ dân cư",i,": ")
    a=int(items2[i]) / float(items1[i])
    print(a)