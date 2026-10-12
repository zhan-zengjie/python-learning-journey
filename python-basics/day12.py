#None 表示空的,无意义的 不使用return语句即返回None None值在判断语句中表示Flase的意思
#定义函数 ，进行文档说明
def add(x,y):
    """
    add函数可以接受两个参数,进行两数相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是两数相加的结果
    """
    result=x+y
    print(f"两数相加的结果是：{result}")
    return result
add(5,6)
#函数的嵌套调用
def fun_b():
    print("---2---")
def fun_a():
    print("---1---")
    fun_b()
    print("---3---")
fun_a()