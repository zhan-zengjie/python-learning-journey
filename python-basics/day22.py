#函数作为参数传递
def test_func(compute):
    result=compute(1,2)
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果是:{result}")
def compute(x,y):
    return x+y
test_func(compute)
#匿名函数
def test_func(compute_):
    result=compute_(1,2)
    print(f"compute_参数的类型是:{type(compute_)}")
    print(f"计算结果是:{result}")
test_func(lambda x,y: x+y)