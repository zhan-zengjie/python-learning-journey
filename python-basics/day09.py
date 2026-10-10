#for循环 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()
#continue中断所在循环的当此执行 直接进入下一次
#break 直接结束所在的循环
#发工资练习
money=10000
for x in range(1,21):
    import random
    score=random.randint(1,10)
    if score<5:
        print(f"员工{x}绩效分为{score},低于5,不发工资,下一位")
        continue
    if money>=1000:
        money-=1000
        print(f"员工{x}满足条件发放1000块钱工资,账户还剩余{money}元")
    else:
        print(f"余额不足，当前余额{money}元，不足以发工资，不发了，下个月再来")
        break


