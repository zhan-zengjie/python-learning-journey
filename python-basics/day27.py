#安装第三方包：在命令提示符内：pip install 包名称
#综合案例
import sys
sys.path.append("D:/python_text")# 把模块所在的路径硬塞给 Python
from my_utils import *
print(str_reverse("黑马程序员"))
print(substr("itheima",0,4))
append_to_file("D:/test_append.txt","itheima")
print_file_info("D:/test_append.txt")