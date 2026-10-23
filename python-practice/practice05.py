#学生成绩排列
students=[
    {'sno':101,'sname':"小张",'sgrade':88},
    {'sno':102,'sname':"小王",'sgrade':77},
    {'sno':103,'sname':"小李",'sgrade':99},
    {'sno':104,'sname':"小赵",'sgrade':66}
]
students_sort1=sorted(students,key=lambda x:x["sgrade"])
students_sort2=sorted(students,key=lambda x:x["sgrade"],reverse=True)
print(f"原列表是:{students}")
print(f"按升序排列后的列表是:{students_sort1}")
print(f"按降序排列后的列表是:{students_sort2}")