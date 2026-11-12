text = "hello world"
count_2={}
for a in text:
    if a==" ":
        continue
    if a in count_2:
        count_2[a]+=1
    else:
        count_2[a]=1
for b in count_2:
    print(f"字母{b}出现了{count_2[b]}次")
for c in count_2:
    if count_2[c]>=2:
        print(f"字母{c}出现次数大于一次")