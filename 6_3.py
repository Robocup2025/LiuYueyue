class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(self.name,self.age,self.gender)
class Student(Person):
    def __init__(self,name,age,gender,college,class_name):
        super().__init__(name,age,gender)
        self.college=college
        self.class_name=class_name
    def personInfo(self):
        super().personInfo()
        print(self.college,self.class_name)
    def __str__(self):
        return f'{self.name} {self.age} {self.gender} {self.college} {self.class_name}'

if __name__ == '__main__':
    x=Person("张三",19,"男")
    x.personInfo()
    y=Student("李四",18,"女","电气学院","电气2401")
    y.personInfo()
    print(y)