#打印区间内的所有素数
def is_primes(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
def print_primes(start,end):
    for i in range (start,end+1):
        if is_primes(i):
            print(f"{i}是一个素数")
start_num=int(input("请输入区间的起始数字:"))
end_num=int(input("请输入区间的结束数字:"))
if start_num > end_num:
    print("起始数字不能大于结束数字！")
else:
    print_primes(start_num,end_num)
#计算圆的面积
import math
r=float(input("请输入圆的半径:"))
def area_of_circle(r):
    area=round(math.pi*r**2,2) #round(浮点数,小数点后要保留的位数)
    return area
print(f"半径为{r}的圆面积为{area_of_circle(r)}")