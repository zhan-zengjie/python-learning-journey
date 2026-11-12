#移除列表中的多个元素

list1=[3,5,7,9,11,13]
list2=[7,11]
#法一
def remove_list(list1,list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1
print(remove_list(list1,list2))
#法二
def remove_list_2(list1,list2):
    return[i for i in list1 if i not in list2]
print(remove_list_2(list1,list2))