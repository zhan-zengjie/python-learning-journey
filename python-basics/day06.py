#while循环一样需要空格缩进 另外需要规划循环终止条件
i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
print(f"1-100累加的和是{sum}")

#获取范围在1-100的随机数字
import random
num=random.randint(1,100)
count=0
flag=True
while flag:
    guess_number=int(input("请输入你猜的数字："))
    count+=1
    if guess_number==num:
        flag=False
        print("恭喜你猜对了")
    else:
        if guess_number<num:
            print("你猜的数字小了")
        else:
            print("你猜的数字大了")
print(f"你一共猜了{count}次")
