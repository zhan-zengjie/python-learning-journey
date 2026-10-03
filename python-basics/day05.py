#布尔类型有两个字面量:True和False
#比较运算符：==，！=，>，<，<=，>=
age1=10
age2=18
print(f"10!=18的结果是:{age1!=age2}")

#if elif else语句一定不要忘记在结尾加: 
#if elif else的代码块都需要4个空格作为缩进
age=int(input("请输入你的年龄:"))
if age>=18:
    print("你已经成年了")
elif age>14:
    print("年龄这么小还能长高")
elif age>8:
    print("要好好长高哦")
else:
    print("小孩子真可爱")
#可以自行嵌套 if elif else 但是需要注意空格缩进 这关系到层级关系