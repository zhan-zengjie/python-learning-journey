try:           #表示接下来的代码可能出现异常
    f=open("D:/text_1.txt","r",encoding="UTF-8") #读取不存在的文件
except Exception as e: #如果有异常则捕获
    print("出现异常")
    f=open("D:/text_1.txt","w",encoding="UTF-8")
else:                  #没有异常则执行接下来的代码
    print("没有异常")
finally:               #有无异常都执行
    f.close()
#异常具有传递性
def func1():
    print("func1开始运行")
    num=1/0  #除以0的异常
    print("func1结束运行")
def func2():
    print("func2开始运行")
    func1()
    print("func2结束运行")
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常,异常的信息时：{e}")
main()