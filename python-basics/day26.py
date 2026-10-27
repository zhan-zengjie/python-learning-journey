#导入模块：
#[from 模块名] import [模块|类|变量|函数|*] [as 别名]
#import time
print("你好")
#time.sleep(5)
print("我好")
import sys
sys.path.append("D:/python_text") # 把模块所在的路径硬塞给 Python
from my_module import *     
test_1(1,2)
test_2(1,2)