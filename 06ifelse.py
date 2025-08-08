# userlists={
#     "Abc":{'name':'abc', 'password':'123'},
#     "Abb":{'name':'abb', 'password':'122'},
#     "Acc":{'name':'acc', 'password':'133'},
#     "Aba":{'name':'aba', 'password':'121'}
# }
# if "Abb" in userlists:
#     print(userlists["Abb"])
 


discounts={7:"50", 12:"40", 15:"30", 18:'20'}

age=int(input("Age:"))

looppa=0
for k,v in discounts.items():
    looppa+=1
    if age<=k:
        print( f'Sizin {v}% endiriminiz var')
        break
    elif age>18:
        print('Sizin 10% endiriminiz var')
    if looppa>0:
        break