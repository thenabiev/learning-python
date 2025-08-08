# name='Sahin'
# age=25

# def hello():
#     name='SVHIN'
#     age=26
#     message=f'Salam menim adim {name}dir menim {age} yasim var'
#     print(message)

# hello()


x='global level'
def enclosing():
    x='enclosing level'
    def innerfunc():
        x='local level'
        print(x)
    innerfunc()

enclosing()