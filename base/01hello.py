# name="Sahin"
# question="Necesen"
# message='Salam {} {}'
# print(message.format(name,question))

# message2=f'Salam {name}'
# print(message2)


################################################################################
# HER HANSISA BIR DEYISENIN MOVCUD BUTUN METODLARINI MUEYYEN ETMEK
# test_str="String metodlari"
# test_list=["Array","Metodlari"]
# test_num=123
# print(
#     dir(test_str)
# )
# print(
#     dir(test_list)
# )
# print(
#     dir(test_num)
# )

def f(x, y=[]):
    y.append(x)
    return y
a=f(1)
b=f(2, [])
c=f(3)
print(a, b, c, a is c)