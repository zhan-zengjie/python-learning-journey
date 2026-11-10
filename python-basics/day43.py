import random
import json
var_1:int=10
var_2:str="itheima"
var_3:bool=True
class Student:
    pass
stu:Student=Student()
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_dict:dict={"itheima":666}
my_list_2:list[int]=[1,2,3]
my_tuple_2:tuple[int,str,bool]=(1,"itheima",True)
my_dict_2:dict[str,int]={"itheima":666}
var_4=random.randint(1,10)               #type:int
var_5=json.loads('{"name":"zhangsan"}')  #type:dict[str,str]
def func():
    return 10
var_6=func()                             #type:int