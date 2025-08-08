# cities=['baku','sumgait','izmir','istanbul','ankara']
# numbers=[2,9,44,67,12]
# print(cities)
# print(help(cities))
# print(len(cities))
# print(cities[-5])
# print(cities[-4:-1])
# print(cities[:-3])

# cities[2]='adana'
# print(cities)
# cities.append('tashkent')
# print(cities)
# cities.insert(2,'izmir')
# print(cities)

##############################################################
# LISTDEN ITEM SILMEK (DEL, POP, REMOVE)

# del cities[cities.index('izmir')]
# print(cities)

# cities.pop()
# print(cities)
# print(cities.pop())

# cities.remove('adana')
# print(cities)

# if cities.index('adana')!=-1:
#     cities.remove('adana')
# print(cities)

# axtarilan_seher=input("Axtar:")
# if cities.count(axtarilan_seher.lower())>0:
#     cities.remove(axtarilan_seher)
#     print(f'{axtarilan_seher} silindi')
# print(cities)


##############################################################
# LISTI SIRALAMAQ


# print(cities)
# cities.sort() metodu listi tamamile deyisir
# cities.sort()
# print(cities)
# cities.sort(reverse=1)
# print(cities)

#sorted(cities) evvelki metoddaan ferqli olaraq burda list deyismir sadece onun deyismis versiyasi print olur
# print(sorted(cities))
# print(cities)
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

####################################################################################################
# ARRAYS PART 2
####################################################################################################

cities=['baku','sumgait','izmir','istanbul','ankara','tbilisi']
people={'China':"Asian", "America":"Mixed", "Niger":"Niggers", "Mexica":"Taco Niggers", "England":"Whites","Japan":"Asian"}
# print(cities.index('sumgait'))

# contains metodu axtarilan itemin listde olub olmamasi cavabini verir
# print(cities.__contains__("baku"))

# city=input("Axtar:")
# if cities.__contains__(city):
#     for i in cities:
#         if i==city:
#             print(f'{i.title()} tapildi')
# else:
#     print("Axtardiginiz seher siyahida yoxdu")


# in metodu
# n=input("Axtar:")
# if n in cities:
#     print(f'{n.title()} tapildi')
# else:
#     print(f'{n.title()} adli seher siyahida yoxdu')

##############################################################

# for city in cities:
#     print(city)

# str_cities='salam men baku amma sumgait ankara istanbul daha tbilisi'
# listcities=str_cities.split(' ')
# print(listcities)

# newList=[]
# for i in listcities:
#     if i in cities:
#         newList.append(i)
#         print(i)
# print(newList)

# n=list(range(10))
# w=[]
# for i in n:
#     w.append(str(i))
# l=".".join(w)
# print(l)


# numbers=[numbre for numbre in range(1,10)]
# print(numbers)


# seherler=cities.copy()
seherler=cities[:]
seherler.append('tabriz')
print(cities)
print(seherler)