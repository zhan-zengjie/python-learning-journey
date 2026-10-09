#for循环中的临时变量(如以下的x)其作用域限定为循环内 如果要访问临时变量 可以预先在循环外定义它
num=0
for x in range(1,100):
    if x%2==0:
        num=num+1
print(f"从1到99一共有{num}个偶数")

i=0
for i in range(1,6):
    print(f"向小美表白的第{i}天")
    for j in range(1,11):
        print(f"今天向小美送出的第{j}多玫瑰花")
    print("小美，我喜欢你")
print(f"向小美表白了{i}天,成功")
#for和while可以互相嵌套