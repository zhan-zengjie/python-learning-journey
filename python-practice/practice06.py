#列表偶数求和
numbers=[1,2,3,4,5,6,7,8,9,10]
sum=0
for num in numbers:
    if num%2==0:
        sum+=num
print(f"列表中所有偶数的和为:{sum}")
#找出年龄最大者
#法一
people={"张三":18,"李四":50,"王五":29,"赵六":22}
max_age=0
max_name=""
for name,age in people.items():
    print(name,age)
    if age>max_age:
        max_age=age
        max_name=name
print(f"年龄最大者的姓名是:{max_name},年龄是:{max_age}岁")
#法二
sorted_people = sorted(people.items(), key=lambda item: item[1],reverse=True)
print(f"年龄最大者的姓名是:{sorted_people[0][0]},年龄是:{sorted_people[0][1]}岁")