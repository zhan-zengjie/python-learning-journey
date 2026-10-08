#while循环的嵌套同样用空格缩进决定层次关系 注意条件控制 避免无限循环
#print语句 输出不换行功能 +,end=''
#特殊符号制表符\t 可以让多行字符串进行对齐
#九九乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    print()
    i+=1  
#for循环： for 变量 in 被处理的数据，与while循环不同 for循环无法定义循环条件
name="sakiko"
for x in name:
    print(x)