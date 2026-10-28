#寻找最小连续9整除数
import sys
sys.set_int_max_str_digits(0)  # 0 表示不限制位数
number=int(input("请输入一个奇数："))
n=1
while True:
    num_9=int('9'*n)
    if num_9%number==0:
        print(f"最小的由{n}个9组成的数{num_9}能整除{number},式子为:{num_9}/{number}={num_9/number}")
        break
    n+=1
#输入整数打印星号
#用户最多输入7个整数
for _ in range(7):
    while True:
        num=int(input("请输入一个整数(1至50之间):"))
        if 1<=num<=50:
            print(num*"*")
            break
        else:
            print("输入无效,请输入一个1至50之间的整数!")
