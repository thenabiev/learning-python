hashira1={"name":"Gyomei","element":"stone", "health":100,'power':90}
# print(type(hashira1))
# print(hashira1)
# print(hashira1['name'])
hashira1['rival']='Kokushibo'
# print(hashira1)
# print(hashira1['clan']) # Bu bize xeta dondurecek cunki dictionarymizde bele key yoxdur bu xeta ile rastlamamaq ucun altdaki usuldan istifade edilir
# print(hashira1.get('clan'))

hashira1.update({'health':120, 'name':"Himejima Gyomei", 'rate':1})

####################################################################################
# Dictionary icindeki herhansi key value deyeri silmek
# del hashira1['rate']
# basqa usul
# hashira1.pop('rival')
# print(hashira1)

# print(hashira1.keys())
# print(hashira1.values())
# print(hashira1.items())
# hashtuples=hashira1.items()
# for i in hashtuples:
#     print(str(i[0]) + ":"+str(i[1]))

# for i in hashira1.keys():
#     print(i)
# for i in hashira1.values():
#     print(i)

my_friends=[
    {'name':'Haci','age':24},
    {'name':'Kamran','age':24},
    {'name':'Orxan','age':23},
]
for i in my_friends:
    print(f'He is my friend {i['name']}, he is {i['age']} old')
