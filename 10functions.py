# list = [1, 'a', 'c', 5]

# def sayilar():

#     for i in list:
#         if type(i)==type(1):
#             print(i)
# sayilar()

def faktorial(a):
    netice=1
    for i in range(1, a+1):
        netice=netice*i
    print(netice)

faktorial(4)