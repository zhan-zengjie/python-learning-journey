class Student:
    name=None                                          #成员变量
    def say_hi(self):                                  #成员方法
        print(f"大家好,我是{self.name},很高心认识大家")  #self不占用参数位置
    def say_hi2(self,msg):
        print(f"大家好,我是{self.name},{msg}")
stu=Student()
stu.name="小明"
stu.say_hi()
stu=Student()
stu.name="小王"
stu.say_hi2("希望大家多多关照")
stu=Student()
stu.name="小红"
stu.say_hi2("欢迎大家来和我交朋友")