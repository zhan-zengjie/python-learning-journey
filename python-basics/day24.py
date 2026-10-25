f=open("D:/text_2.txt","w",encoding="UTF-8")#若文件已存在 则覆盖文件原内容
f.write("Hello world!!!")#内容写入到内存中
f.flush()#将内存中积攒的内容，写入到硬盘的文件中
f.close()#close方法 内置了flush的功能
f=open("D:/text_2.txt","a",encoding="UTF-8")#若文件已存在 不覆盖文件原内容
f.write("\n你好,世界!!!")
f.close()

fr=open("D:/bill.txt","r",encoding="UTF-8")
fw=open("D:/bill_2.txt","w",encoding="UTF-8")
for line in fr:
    line=line.strip()
    if line.split(",")[4]=="测试":
        continue
    fw.write(line)
    fw.write("\n")
fr.close
fw.close