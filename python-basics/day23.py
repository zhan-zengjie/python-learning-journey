#通过文件读取操作 读取文件 统计itheima单词出现的次数
#法一
f=open("D:/text.txt","r",encoding="UTF-8")
content=f.read()
count=content.count("itheima")
print(f"itheima在文件中出现了{count}次")
f.close()
#法二
f=open("D:/text.txt","r",encoding="UTF-8")
count_1=0
for line in f:
    line=line.replace("\n","")
    words=line.split(" ")
    for word in words:
        if word=="itheima":
            count_1+=1
print(f"itheima在文件中出现了{count_1}次")
f.close()
#法二的另一种写法
f=open("D:/text.txt","r",encoding="UTF-8")
count_2=0
for line in f:
    line=line.strip() #去掉开头和结尾的空格及换行符
    words=line.split(" ")
    for word in words:
        if word=="itheima":
            count_2+=1
print(f"itheima在文件中出现了{count_2}次")
f.close()