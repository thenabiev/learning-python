# n=1
# while n<10:
#     print(n)
#     n+=1


# message=''
# while message!='quit':
#     message=input('Quit yazana qeder davam : ')
#     print(message)


# myFlag=True
# message=''

# while myFlag:
#     message=input('Type "quit" for escape from loop : ')
#     if message=='quit':
#         myFlag=False
#     else:
#         print(message)


num=0
while num<10:
    num+=1
    if num%2==0:
        continue
    print(num)