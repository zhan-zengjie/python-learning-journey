class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
student_list = []
total_students = 3
for i in range(1, total_students + 1):
    print(f"当前录入第{i}位学生信息，总共需录入{total_students}位学生信息")
    name = input("请输入学生姓名： ")
    age = input("请输入学生年龄： ")  
    address = input("请输入学生地址： ")
    stu = Student(name, age, address)
    student_list.append(stu)
    print(f"学生{i}信息录入完成，信息为：[学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}]")
print("\n========== 全部学生信息录入完毕 ==========")
for stu in student_list:
    print(f"姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}")