#按序插入列表
list=[21,33,57,88,95]
num=int(input("请输入一个数字："))
for i in range(len(list)):
    if num<list[i]:
        list.insert(i,num)
        break
else:
    list.append(num)
print(list)
#输入数字排序
num_1=float(input("请输入一个数字："))
num_2=float(input("请输入一个数字："))
num_3=float(input("请输入一个数字："))
list=sorted([num_1,num_2,num_3])
print(f"按照从小到大排序:{list}")