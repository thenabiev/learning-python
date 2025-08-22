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
    
    
    # @classmethod
    # def displaySchoolName(cls, nameOfSchool):
    #     cls.mekteb=nameOfSchool
    
    # @staticmethod
    # def statik():
    #     return f'Im just sending this message'
    # def riy(num):
    #     return num*2


        
student1=Student("Sahin", 25, {"Informatika":99, "English":70, "Russian":51})
student2=Student("Esli", 22, {"Informatika":70, "English":90, "Russian":60})

# print(student1.mekteb)
# Student.displaySchoolName("Y Sayli mekteb")
# print(student1.mekteb)

# print(student1.statik())
# print(Student.riy(3))


# print(Student.numberofstudents)

# print(student1.average())
# print(student1.mekteb)
# print(student2.mekteb)
# print(student2.__dict__)



##########################################################################

# class UniversityStudent(Student):
#     def __init__(self, name, age, grades, university):
#         super().__init__(name, age, grades)
#         self.university=university

# uStudent1=UniversityStudent("Piti", 20, {"Informatika":100, "English":71, "Russian":51}, "ADIU")
# print(uStudent1.__dict__)
# print(uStudent1.average())
# print(uStudent1.average())
# print(help(UniversityStudent))



# class Circle : 
#     pi=3.14
#     def __init__(self, radius):
#         self.radius=radius

#     def area(self):
#         return self.pi*self.radius**2 
    
#     def __repr__(self):
#         return f'{__class__.__name__}, {self.area()}, {self.radius}'
    
# daire=Circle(5)
# print(daire.area())
# print(daire.__repr__())

class Student :
    def __init__(self, name, surname, age, grades):
        self.name=name;
        self.surname=surname;
        self.age=age;
        self.grades=grades;
    
    @property
    def average(self):
        return sum(self.grades)/len(self.grades)
    
    @property
    def fullname(self):
        return self.name+ ' '+self.surname
        

student1=Student("Sahin", "Nabiev", 25, [28,17,31,24])
print(student1.average)
print(student1.fullname)