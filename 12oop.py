# class Car:
#     def __init__(self, brand, model, year, color):
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.color=color
#     def brandModel(self):
#         return f'Marka {self.brand}, model {self.model}'

# car1=Car("Ford", "F-150", 2016, 'Black')
# car2=Car("Toyota", "Hilux", 2012, 'White')

# print(car1.color)
# print(car1.brandModel())

# listofCars=[]

# def addCar():
#     brand=input('Brand')
#     model=input('Model')
#     year=int(input('Year'))
#     color=input('Color')

#     listofCars.append(Car(brand, model, year, color ))
#     print(listofCars[0].model)

# addCar()


##########################################################################

# class Movie():
#     def __init__(self, name, theme, year):
#         self.name=name
#         self.theme=theme
#         self.year=year
#     def fullName(self):
#         return f'{self.name} {self.year}'

# movie1=Movie("Transfoemers", 'Action', 2010)
# print(movie1.fullName())

###########################################################################

class Student:
    mekteb='X sayli tam orta mekteb'
    capacity=500
    numberofstudents=0
    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
        Student.numberofstudents+=1
    def average(self):
        s=0
        for i in self.grades.values():
            s=s+i
        return f'{self.name} : {s//len(self.grades)}'
        
student1=Student("Sahin", 25, {"Informatika":99, "English":70, "Russian":51})
student2=Student("Esli", 22, {"Informatika":70, "English":90, "Russian":60})

print(Student.numberofstudents)

# print(student1.average())
print(student1.mekteb)
print(student2.mekteb)
print(student2.__dict__)



##########################################################################

