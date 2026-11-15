# 变量互换
def swap_values(var1, var2):
    return var2, var1


num1 = 10
num2 = 13
num1, num2 = swap_values(num1, num2)  # 或者直接num1,num2=num2,num1
print(f"num1:{num1},num2:{num2}")

# 计算字典值参数
example_dict = {"a": 100, "b": 200, "c": 300}


# 法一
def sum_of_dict_values(my_dict):
    result = 0
    for value in my_dict.values():
        result += value
    return result


print(sum_of_dict_values(example_dict))


# 法二
def sum_of_dict_values_2(my_dict):
    return sum(my_dict.values())


print(sum_of_dict_values_2(example_dict))
