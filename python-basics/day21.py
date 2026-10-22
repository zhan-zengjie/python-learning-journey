def return_test():
    return 2,"hello",True
x,y,z=return_test()
print(x)
print(y)
print(z)
def user_info(name,age,gender):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")
#位置参数
user_info("小明",8,"男")
#关键字参数
user_info(age=6,name="小红",gender="女")
#位置参数和关键字参数混合 位置参数需在前
user_info("小桃",10,gender="女")
#缺省参数 设置默认值必须在最后
def user_info(name,age,gender="男"):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")
user_info("小天",9)
user_info("小甜",10,gender="女")
#不定长参数
#位置传递 以元组形式接受参数
def user_info(*args):
    print(f"args参数的类型是:{type(args)},内容是:{args}")
user_info(1,2,3,"小明","男孩")
#关键字传递 以字典形式接受参数
def user_info(**kwargs):
    print(f"kwargs参数的类型是:{type(kwargs)},内容是:{kwargs}")
user_info(age=6,name="小红",gender="女")