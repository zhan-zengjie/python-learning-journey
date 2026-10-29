import json
data=[{"name":"小明","age":13},{"name":"小红","age":17},{"name":"小王","age":18}]
json_str=json.dumps(data,ensure_ascii=False)#如果不含中文则不需要加ensure_ascii=False
print(type(json_str))
print(json_str)
d={"name":"小李","age":11}
json_str=json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)
s='[{"name": "小明", "age": 13}, {"name": "小红", "age": 17}, {"name": "小王", "age": 18}]'
l=json.loads(s)
print(type(l))
print(l)
s='{"name": "小李", "age": 11}'
d=json.loads(s)
print(type(d))
print(d)