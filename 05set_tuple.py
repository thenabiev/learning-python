################################################################################################
############################################## TUPLE ###########################################
capitals=('baku', 'ankara', 'london','tokyo','berlin')
# print(len(capitals))
# print(capitals[3])
# print(capitals[2:5], capitals[2:], capitals[-3:-1], capitals[-3:], sep='\n')


################################################################################################
# tuplelarin elementlerini adi listler kimi deyismek olmur meselen altdaki numunede error alariq
# capitals[0]='istanbul'
# for i in range(0,len(capitals)):
#     capitals[i]='deyisdi'
# print(capitals)
################################################################################################

# tupleleri umumi sekilde deyismek mumkundur. meselen
# capitals1=('baku', 'ankara', 'london','tokyo','berlin')
# capitals1=('sumqayit', 'istanbul', 'manchester', 'kyoto', 'bayern')
# print(capitals1)

################################################################################################
############################################### SET ############################################

# set_cities={'sumqayit', 'istanbul', 'manchester', 'kyoto', 'bayern'}
# print(type(set_cities))
# print(set_cities[0]) # Error verecek
# set_cities.add('roma')
# print(set_cities)

# set_cities.update(['amsterdam','mexico'])
# print(sorted(set_cities))

# set_cities.remove('mexico')
# print(set_cities)
# remove metodu ile set icinde olmayan elementi silmeye calissaq xeta alariq bu xetani almamaq ucun discard metodundan istifade ede bilerik
# set_cities.discard('paris')
# print(set_cities)

# seti tamamen temizlemek ucun - clear()
# set_cities.clear()
# print(set_cities)

# seti tamamen silmek ucun - del (bu usuldan sonra print etmeye calissaq xeta alariq)
# del set_cities
# print(set_cities) # error


################################################################################################
############################################ PRAKTIKA ##########################################
# Task 1
cities=('baku', 'ankara', 'london','tokyo','berlin','sydney')
# son elementi yazdir
# print(cities[-1])
# son 3 elementi yazdir
# print(cities[-3:])
# ilk 2 elementi yazdir
# print(cities[:2])

# Task 2
# nwtuple=('sumqayit', [28, 'Svhin'], (2,4,6), 100)
# print sumqayit
# print(nwtuple[0])
# print Svhin
# print(nwtuple[1][1])
# list icindeki tuple elementin son alt elementini yazdir
# for i in nwtuple:
#     if type(i)==tuple:
#         print(i[-1]) 

# newtuple=(4, 2, [1, 20])
# print(newtuple)
# newtuple[-1][0]=100
# print(newtuple)

#####################################################################
ntuple=('baku', 'ankara', 'london','baku','tokyo','berlin','sydney','berlin','ankara')
# tuple elementi set elemente cevirmek
nset=set(ntuple)
print(nset)

# set elementi tuple elemente cevirmek
ntuple2=tuple(nset)
print(ntuple2)

#####################################################################
names={"Esli", "Sahin", "Mamasini", "Piti", "Nyx", "Miki"}
names.add("agamirze")
print(names)
linames=list(names)
print(linames)

#######################################################################
nwords='niggerniggerniggernigger'
# nwordlist=[]
# for i in nwords:
#     if i=='g':
#         if nwordlist.count(i)<=1:
#             nwordlist.append(i)

#     if nwordlist.count(i)==0:
#         nwordlist.append(i)

# nword="".join(nwordlist)
# print(nword.upper()) 

newnset={niger for niger in nwords}
print(newnset)