friends=['lucy','nyu','nana','kazami','khouta','kanae']
"""
friends listindeki 'kazami' xaric butun elementleri while ve for dovrleri ile cap et
"""
# i=0
# while i<len(friends):
#     if friends[i]!='kazami':
#         print(friends[i])
#     i=i+1

# for i in friends:
#     if i!='kazami':
#         print(i)


"""
User terefinden girilen iki eded arasindaki cut ededleri yazin
"""
# num1=int(input("Num 1 : "))
# num2=int(input("Num 2 : "))

# if num1>num2:
#     for i in range(num2, num1+1):
#         if i%2==0:
#             print(i)
# else:
#     for i in range(num1, num2+1):
#         if i%2==0:
#             print(i)


"""
While loop ile 1 ile 100 arasindaki eded texmini ede bileceyimiz proqram yazin
"""
# import random
# xnum=random.randint(1,100)
# print(xnum)

# x=int(input('X : '))

# while x!=xnum:
#     if x<xnum:
#         x=int(input('Daha boyuk reqem olmalidi : '))
#     else:
#         x=int(input('Daha kicik reqem olmalidi : '))
        

# print("Dogrudur! Ne bildin ala")
# print("Oyun bitdi")


"""
celciuses=[20, 25, 30, 35] derecelerini Kelvin ve Fahrenheit standartlarina gore goster
K=C+273
F=C*9/5+32
"""

celciuses=[20, 25, 30, 35]
kelvin=[]
fahrenheit=[]

for c in celciuses:
    k=c+273
    f= c*9/5+32
    kelvin.append(k)
    fahrenheit.append(f)
    print(f'C - {c}')
    print(f'K - {k}')
    print(f'F - {f}')
    print('-----------------------')

print(kelvin)
print(fahrenheit)