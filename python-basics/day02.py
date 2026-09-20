#定义一个变量，记录钱包的金额
money=100
print("我的钱包有",money,"元")
#我买了东西 钱包余额发生变化
money=money-5.5
print("买了一个冰淇淋，我的钱包剩余",money,"元")


#查看数据类型
#方法一
print(type("我的钱包"))
#方法二
string_type=type("我的钱包")
int_type=type(100)
float_type=type(5.5)
print(string_type)
print(int_type)
print(float_type)
#方法三
money_type=type(money)
print(money_type)

#关于数据类型的转换，公式为 str(),int(),float()
#以整数转成字符串为例子
print(type(str(11)))