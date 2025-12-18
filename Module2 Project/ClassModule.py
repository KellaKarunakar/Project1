#This File be used as a module this time for the classes. It is possible to import the classes and cto crate the objects in the another python file.

class Student:
    count =0 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        Student.count +=1
    def display(self):
        print(f"The student name is {self.name} and the age of the student is {self.age}")
    def get_count():
        print(f"There are total {Student.count} students in the class...")