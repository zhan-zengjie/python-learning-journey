#计算1到100的整数和
num=0
for x in range(1,101):
    num+=x
print(f"1到100的整数和是:{num}")
#统计1~4组成的三位数
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                print(i,j,k)
                count+=1
print(f"数字1,2,3,4能组成{count}个互不相同且无重复数字的三位数")