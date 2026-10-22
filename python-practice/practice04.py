#统计字符类型个数
my_str=input("请输入一个字符串:")
letters=0
space=0
digit=0
others=0
for i in my_str:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        others+=1
print(f"英文字母字符有{letters}个,数字有{digit}个,空格有{space}个,其他字符有{others}个")
#对简单列表进行排序
#改变原序列
list1=[3,4,2,1,9,5]
list1.sort()#升序
print(list1)
list1=[3,4,2,1,9,5]
list1.sort(reverse=True)#降序
print(list1)
#不改变原序列 返回新列表
list1=[3,4,2,1,9,5]
list2=sorted(list1)#升序
list3=sorted(list1,reverse=True)#降序
print(f"list1:{list1}")
print(f"list2:{list2}")
print(f"list3:{list3}")