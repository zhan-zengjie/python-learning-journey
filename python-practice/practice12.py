#计算整数的阶乘
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
user_input = input("请输入一个数字: ")
try:
    num_float = float(user_input)
    if not num_float.is_integer():#判断是否为小数
        print("错误：阶乘不能是小数，请输入整数！")
    elif num_float < 0:#判断是否为负数
        print("错误：负数没有阶乘！")
    else:
        num = int(num_float)
        print(f"{num} 的阶乘结果为: {factorial(num)}")
except ValueError:
    print("错误：您输入的不是数字，请输入一个数字！")