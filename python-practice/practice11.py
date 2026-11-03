#计算连续数字串和
#法一
num=input("请输入一个数字:")
n=int(input("请输入加数的个数:"))
result=0
for i in range(1,n+1):
    result+=int(i*num)
print(f"计算和为:{result}")
#法二
num=int(input("请输入一个数字:"))
n=int(input("请输入加数的个数:"))
result=0
current_term=0
for i in range(1,n+1):
    current_term=current_term*10+num
    result+=current_term
print(f"计算和为:{result}")