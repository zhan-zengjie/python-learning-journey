#进制转换
num=int(input("请输入一个数字："))
print(f"十进制为:{num}")
print(f"转换为二进制为{bin(num)}")
print(f"转换为八进制为{oct(num)}")
print(f"转换为十六进制为{hex(num)}")
#平方运算
while True:
    i=int(input("请输入一个数字:"))
    result=i**2
    print(f"数字{i}的平方运算结果是{result}")
    if result<50:
        print("平方运算结果小于50,程序结束")
        break