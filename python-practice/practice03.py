#需求：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#以后每天早上都吃了前一天剩下的一半零一个，到第 10 天早上想再吃时，见只剩下一个桃子了，求第一天共摘了多少个。
#法一
day=1
peaches=1
while day<10:
    peaches=(peaches+1)*2
    day+=1
print(f"第1天摘了{peaches}个桃子")
#法二
peaches=1
for _ in range(9):
    peaches=(peaches+1)*2
print(f"第1天摘了{peaches}个桃子")
#法三
peaches=1
for day in range(9,0,-1):
    peaches=(peaches+1)*2
print(f"第{day}天摘了{peaches}个桃子")#如果要求1~9天每天桃子的数量 则把此句加入for 循环语句中