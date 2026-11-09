#求范围内所有的偶数
#法一
def get_even_numbers(start,end):
    my_list=[]
    for i in range(start,end+1):
        if i%2==0:
            my_list.append(i)
    return my_list
start=int(input("请输入起始数字:"))
end=int(input("请输入结束数字:"))
print(get_even_numbers(start,end))
#法二
def get_even_numbers_2(start,end):
    return [i for i in range(start,end+1) if i%2==0]
start=int(input("请输入起始数字:"))
end=int(input("请输入结束数字:"))
print(get_even_numbers_2(start,end))