#列表的方法
#列表.append(元素)，列表.extend(容器)，列表.insert(下标,元素)，del 列表[下标]，列表.pop(下标)
#列表.remove(元素)，列表.clear()，列表.count()，列表.index(元素)，len(列表)
mylist=[21,25,21,23,22,20]
mylist.append(31)
mylist.extend([29,33,30])
num1=mylist[0]
print(f"列表中的第一个元素为:{num1}")
num2=mylist[-1]
print(f"列表中的最后一个元素为:{num2}")
index=mylist.index(31)
print(f"元素31在列表的下标位置是{index}")
print(f"最后的列表内容为{mylist}")
index=0
while index<len(mylist):
    element=mylist[index]
    print(f"列表的元素:{element}")
    index+=1
for element in mylist:
    print(f"列表的元素有：{element}")