#列表元素去重
list1=[10,20,30,10,20]
#法一
def remove_duplicates(list1):
    list2=[]
    for i in list1:
            if i not in list2:
                list2.append(i)
    return list2
print(remove_duplicates(list1))
#法二
def remove_duplicates2(list1):
     return list(set(list1))
print(remove_duplicates2(list1))