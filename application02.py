dersler=['fizika','informatika','riyaziyyat','azerbaycan dili','ingilis dili']

# IKINCI VE SONUNCU ITEMIN ADININ BAS HERFLERI BOYUK YAZ
# print(dersler[1].title(), dersler[len(dersler)-1].title())

# LISTIN SON ITEMINI len() metodu olmadan tapmaq
# print(dersler[-1])

# INFORMATIKA VE RIYAZIYYAT ITEMLERINI AL
# print(dersler[1:3])

# ILK IKI ITEMI YAZDIR
# print(dersler[0:2])
# print(dersler[:2])

# SON IKI ELEMENTI YAZDIR
# print(dersler[-2:])

# NESTED LIST ICINDEKI BUTUN ELEMENTLERI SERBEST YAZMAQ
# dersler2=['fizika',['informatika','kimya'],'riyaziyyat','azerbaycan dili','ingilis dili']

# for i in dersler2:
#     if type(i)==type(dersler2):
#         for j in i:
#             print(j)
#     else :
#         print(i)

# dersler LISTININ UZUNLUGUNU GOSTER
# print(len(dersler))
# veya
# l=0
# for i in dersler:
#     l=l+1
# print(l)

# KIMYA FENNINI LISTE ELAVE ET (SONA, ORTAYA BASA)
# dersler.append("kimya")
# dersler.insert(
#     len(dersler)//2 , 'kimya'
# )
# dersler.insert(0,'kimya')
# dersler[len(dersler):]=['kimya']
# dersler.insert(len(dersler),'kimya')

# del metodu ile kimya elementini sil
# del dersler[5]
# del dersler[dersler.index('kimya')]
# dersler.remove('kimya')
# dersler.remove(dersler[5])
# print(dersler)


numbers=[8,4,5,3,7,11,2,9]

#listi artan ve azalan sira ile duz
# print(sorted(numbers))
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=1)
# print(numbers)

dersler3=[['fizika','informatika'],['riyaziyyat','azerbaycan dili'],['ingilis dili','kimya']]
# dersler3 listindeki elementlerin son elementleri ile yeni bir list qur
# nw=[]
# for f in dersler3:
#     nw.append(f[-1])
# print(nw)


# 1-10 parcasindaki ededlerin kvadratlarindan ibaret list yarat
# eyni isi list comprension ile de et
# eyni prosesi hemin araliqdaki cut ededler ucun et
nwl=[]
for i in range(1,11):
    nwl.append(i**2)

nwl2=[nombr*nombr for nombr in range(1,11)]

nwlcut=[nom*nom for nom in range(1,11) if nom%2==0]

print(nwl)
print(nwl2)
print(nwlcut)

