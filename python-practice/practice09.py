#判断数字奇偶性
num=int(input("请输入一个数字:"))
if num%2==0:
    print(f"{num}是一个偶数")
else:
    print(f"{num}是一个奇数")
#判断年份是否为闰年
num_2=int(input("请输入一个数字:"))
if (num_2%4==0 and num_2%100!=0) or num_2%400==0:
    print(f"{num_2}是闰年")
else:
        print(f"{num_2}不是闰年")