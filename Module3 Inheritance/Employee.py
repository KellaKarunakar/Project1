from Person import Person 

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age) 
        self.salary = salary 
    def display(self):
        print(self.name , self.age, self.salary) # here this method depicts the method overriding. The attributes that we are using self.name, self.age are initialized when the super constructor is called. 

