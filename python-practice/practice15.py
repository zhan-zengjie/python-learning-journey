#求前N个数字的平方和
def sum_of_squares(N):
    result=0
    for i in range (1,N+1):
        result+=i**2
    return result
print(sum_of_squares(int(input("请输入一个数字:"))))
#计算给定列表数字的和
def sum_of_list(number_list):
    return sum(number_list)
list1=[1,2,3,4]
list2=[20,4,8,21,15,25]
print(sum_of_list(list1))
print(sum_of_list(list2))