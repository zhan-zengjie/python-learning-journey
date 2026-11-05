class Student:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("Student类创建了一个类对象")
stu=Student("小明",18,"18500002222")
print(stu.name)
print(stu.age)
print(stu.tel)