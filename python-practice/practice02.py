#九九乘法表
for i in range(1,10):
    for k in range (1,i+1):
        print(f"{k}*{i}={k*i}\t",end="")
    print()
#找出所有的水仙花数（一个三位数，其各数数字立方和等于该数本身）
#法一
for x in range(1,10):
    for y in range(10):
        for z in range(10):
            if 100*x+10*y+z==x**3+y**3+z**3: #更好的写法是 num=int(f"{x}{y}{z}")
                                                         #if num ==x**3+y**3+z**3:            
                print(f"{x}{y}{z}")
#法二
for num in range(100,1000):
    a=num//100
    b=num//10%10
    c=num%10
    if num==a**3+b**3+c**3:
        print(num)