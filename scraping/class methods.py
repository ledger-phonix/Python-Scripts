class Employee:
    CompanyName = 'Apple'
    def show(self):
        print(f'The name of employee is {self.name} and the company is {self.CompanyName}. ')
    @classmethod #to change the class variable
    def changeCompany(cls, newCompany):
        cls.CompanyName = newCompany
e1 = Employee()
e1.name = 'Talha'
e1.show()
e1.changeCompany('Tesla')
e1.show()
print(Employee.CompanyName)
#see the class variable not change , we will use decorator

print('\n')
class Person:
    def __init__(self,name, salary):
        self.name= name
        self.salary=salary
    
    @classmethod
    def fromStr(cls,string):
        return cls(string.split('-')[0],int(string.split('-')[1]))


e = Person('Talha' ,1200)
print(e.name)
print(e.salary)
print('\n')

string = 'Harry-4000'
e1 = Person.fromStr(string)
print(e1.name)
print(e1.salary)
print(type(e1.salary)) 
