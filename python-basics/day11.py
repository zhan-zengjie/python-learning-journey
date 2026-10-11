def add(x,y,z):
    result=x+y+z
    print(f"{x}+{y}+{z}的计算结果是：{result}")
add(5,6,7)
#练习
def check(age):
    print("欢迎光临,请出示你的身份证")
    if age<=6:
        print(f"你的年龄是{age}岁，免费游玩")
    else:
        print(f"你的年龄是{age}岁，需要购票")
check(6)

def sum(a,b):
    num=a+b
    return num
f=sum(8,6)
print(f)