# 计算斐波那契数列的第n项
def validate_input(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("输入错误：请输入一个纯整数")
    if n <= 0:
        raise ValueError("范围错误：请输入一个正整数")
    return n


def fibonacci_dict(n):
    n = validate_input(n)
    my_dict = {1: 1, 2: 1}
    for i in range(3, n + 1):
        my_dict[i] = my_dict[i - 1] + my_dict[i - 2]
    return my_dict[n]


def fibonacci_recursive(n):
    n = validate_input(n)
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


user_input = input("请输入一个正整数:")
try:
    print(fibonacci_dict(user_input))
    print(fibonacci_recursive(user_input))
except ValueError as e:
    print(f"错误提示：{e}")
