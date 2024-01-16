# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


# def average(sequence):
#     return sum(sequence) / len(sequence)


# print(average(student["grades"]))

# # But wouldn't it be nice if we could...
# # print(student.average()) ?


# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (89, 90, 93, 78, 90)

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student()
# print(student.average())
# # Identical to Student.average(student)


# # -- Parameters in __init__ --


# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student("Bob", (36, 67, 90, 100, 100))
# print(student.average())

# # -- Remember *args ? --


# class Student:
#     def __init__(self, name, *grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student("Bob", 36, 67, 90, 100, 100)
# print(student.average())

class Student: 
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
        
    def average(self):
        return sum(self.grades)/len(self.grades)
        
student = Student("Bob",(100,90,93,78,90))
student2 = Student("FRaser",(10,90,93,78,90))
student.age = 12

student.child = ''
if student.age > 11:
    student.child = True
else:
    student.child = False

# if student.child == True:
#     print(f'{student.name} is a child')
# else:
#     print(f'{student.name} is a not child')

#this is calling the average method that is inside the class Student and the self will be student which contants .name/.grades
# print(Student.average(student))

#does the same lol
print(student.name)
print(student.grades)
print(student.average())

print(student2.name)
print(student2.grades)
print(student2.average())
    

