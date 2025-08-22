# class Dawg:
#     def __init__(self, name, age):
#         self.name=name;
#         self.age=age

#     def myDawgName(self):
#         return f'Blablablableblebleblublublu {self.name}'
        

# bomboclat=Dawg('Dawg', 12);
# print(bomboclat.myDawgName())

# class Dawg:
#     num_legs=4

#     def __init__(self, name):
#         self.name=name

# dawg1=Dawg("Tarzan")
# dawg2=Dawg("Wody")

# print(dawg1.num_legs)
        

class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
    
    def __str__(self):
        return self.name+' '+self.surname+' '+str(self.age)
    

person1=Person("Sahin", "Nabiev", 25) 
print(person1.__str__())


class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary=salary

    def __str__(self):
        return super().__str__() +' '+ str(self.salary)
    
emp1=Employee("Sahin", "Nabiev", 25, 2000)
print(emp1.__str__())