# my_file=open('movies.txt', 'r')
# file_content=my_file.read()
# print(file_content)
# print(my_file.name)
# print(my_file.mode)
# my_file.close()
# print(my_file.read())
# print(file_content)


#################################################################
 
# with open('movies.txt') as myFile :
#     # print(myFile.read())
#     # print(myFile.readline())
#     # print(len(myFile.readlines()))

#     # for i in range(4):
#     #     print(myFile.readline())

#     for line in myFile:
#         print(line)


##########################################################

transferingData=''

with open('movies.txt', 'r') as my_file:
    transferingData=my_file.read()


# with open("data.txt", 'w') as data:
    # data.write(transferingData+'\n')
    # data.write("Racing\n")
    # data.write("Rampage")
    # print(data.readable())
    ################################
    # data.write("Elysium")
    # data.seek(2)
    # data.write("Devil may cry")
    ################################
    # data.write('Star wars 3\n')
    # print("Shrek", file=data)

##############################################################
# with open("data.txt",'a') as data:
#     data.write("Batman\n")
#     data.write("Van Helsing")
    

###############################################################
with open("data2.txt", 'x') as data2:
    data2.write("Salam")