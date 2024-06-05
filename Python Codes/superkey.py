class  Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang
rohan = Employee('Talha',2)
rohan1 = Programmer('Nadeem',3, 'python' )
print(rohan.name)
print(rohan1.id)