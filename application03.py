friends={"Haci":24, "Kamran":23, "Orxan":23}

#########################################################################
# summ=0
# for i in friends.values():
#     summ+=i
# print(summ / len(friends))
# print(sum(friends.values()))
#########################################################################

# friends['Elmin']=29
# print(friends)

friends.update({"Elmin":29, "Nigger":31})

# friends.pop("Nigger")
# print(friends)

# del friends['Nigger']

# friends.update({"Elmin":28})
# print(friends)


######################################################################

mydict={'oddnumbers':[1,2,3]}

# for i in range(len(mydict["oddnumbers"])):
#     mydict["oddnumbers"][i]=mydict["oddnumbers"][i]**2

# print(mydict)

# for i in mydict.values():
#     nwList=[]
#     for j in i:
#         nwList.append(j*j)

# print(nwList)
# mydict.update({'oddnumbers':nwList})
# print(mydict)


###########################################################################
myFriends={"Abc":20, "Bca":22}
###############
# names=[]
# ages=[]
# for i in myFriends.keys():
#     names.append(i)

# for i in myFriends.values():
#     ages.append(i+1)

# print(names, ages , sep='\n')

# newfriends=dict(zip(names,ages))
# print(myFriends)
# print(newfriends)
###############

# keylist=[]
# valuelist=[]

# for k,v in myFriends.items():
#     keylist.append(k)
#     valuelist.append(v)
#     print(keylist, valuelist, sep='\n')
#     print(sum(valuelist))

####################################################################

newdict={x:x**2 for x in range(1,11)}
print(newdict)