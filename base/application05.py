"""
###############################################################
Girilen ededin cut ya tek oldugunu bildiren ifade yaz
###############################################################
"""


# n=int(
#     input('Enter number: ')
# )
# if n%2==0:
#     print(f'{n} - is even number')
# else:
#     print(f'{n} - is odd number')


"""
#################################################################
Girilen ededin musbet, menfi veya sifir oldugunu gosteren kod yaz
#################################################################
"""


# m=int(input("Add a number: "))
# if m==0:
#     print(f'{m} = Zero')
# elif m>0:
#     print(f'{m} is Positive')
# else:
#     print(f'{m} is Niggative')


"""
#################################################################
x=10
y=5
if x>y :
    print(f'{x} ededi {y} ededinden boyukdur')
ifadesini ternary operator ile yaz
#################################################################
"""


# x=int(input('X : '))
# y=int(input('Y : '))
# print(f'{x} ededi {y} ededinden boyukdur') if x>y else print(f'{x} ededi {y} ededinden kicikdir')


"""
#################################################################
Giriilen herhansi bir ededin faktorialini tapin
#################################################################
"""


# f=int(input('F: '))
# if f==0:
#     print(f'{f}!=1')
# elif f>0:
#     n=1
#     for i in range(1,f+1):
#         n=n*i
#     print(f'{f}!={n}')
# else:
#     n=1
#     for i in range(1,abs(f)+1):
#         n=n*i
#         print(n,i)
#     print(f'{f}!={-n}')


"""
#################################################################
notes={"Sahin":58,"Jamal":50,"Memmed":76,"Aide":90,"Abbas":44}
51 v' yuxari bal yazanlar kecdi yazsin asagilar kesildi
#################################################################
"""


notes={"Sahin":58,"Jamal":50,"Memmed":76,"Aide":90,"Abbas":44}
# for k,v in notes.items():
#     if v>50:
#         print(f'{k} imtahandan kecdi')
#     else:
#         print(f'{k} yarra yedi')

name=input("Ad:")

# telebe=notes.get(name)
# print(telebe)

# if telebe>50:
#     print(f'{name} imtahandan kecdi')
# else:
#     print(f'{name} yarra yedi')
#################################
# telebe=notes[name.title()]
# if telebe>50:
#     print(f'{name.title()} imtahandan kecdi')
# else:
#     print(f'{name.title()} yarra yedi')
