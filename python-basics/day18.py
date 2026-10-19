#集合可以修改 ；集合自动去重
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(set3)   #set1 set2 内容不变
set1.difference_update(set2)
print(set1)  #set2内容不变
set4=set1.union(set2) #合并
print(set4)
#集合是无序的 不允许下标索引访问 所以不能用while循环遍历
for element in set1:
    print(f"集合set1的元素有:{element}")

my_list=[1,3,5,2,1,4,3,5,5,1]
my_set=set()
for element in my_list:
    my_set.add(element)
print(my_set)