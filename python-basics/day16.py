#元组一旦完成定义 就不可修改，元组中嵌套的列表的元素可以修改
#如果元组后面只有一个数据，这个数据后面要添加逗号
#元组的方法：列表.index(元素)，len(列表)，列表.count()
student_info = ('周杰伦', 11, ['football', 'music'])
age_index = student_info.index(11)
print(f"年龄所在的下标位置是: {age_index}")
name = student_info[0]
print(f"学生的姓名是: {name}")
student_info[2].remove('football')
print(f"删除football后的爱好列表: {student_info[2]}")
student_info[2].append('coding')
print(f"增加coding后的爱好列表: {student_info[2]}")
print(f"最终元组内容为: {student_info}")
#字符串.replace(字符串1,字符串2) 将字符串内的全部字符串1替换为字符串2
#字符串.split(字符串) 按照给定的字符串对字符串进行分割
#字符串.strip()，字符串.strip(字符串) 移除首尾的空格和换行符或指定字符串
my_str="itheima itcast boxuegu"
num=my_str.count("it")
print(f"字符串{my_str}中有{num}个it字符")
new_my_str=my_str.replace(" ","|")
print(f"字符串{my_str}被替换空格后，结果是：{new_my_str}")
my_str_list=new_my_str.split("|")
print(f"字符串{new_my_str}按照|分割结果是：{my_str_list}")