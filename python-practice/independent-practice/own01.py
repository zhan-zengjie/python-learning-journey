nums = [1, 2, 3, 2, 4, 3, 3, 5]
nums_2=[]
nums_3=[]
for i in nums:
    if i not in nums_2:
        nums_2.append(i)
for j in nums_2:
    nums.remove(j)
for k in nums:
    if k not in nums_3:
        nums_3.append(k)
for x in nums_3:
    print(x)