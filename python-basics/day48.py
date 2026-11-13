from pyecharts.charts import Bar

region_total = {}
total = 0
with open(r"D:\code_work\python-basics\sales_data.csv", "r", encoding="utf-8") as f:
    f.readline()
    for line in f:
        parts = line.strip().split(",")
        amount = int(parts[2]) * int(parts[3])
        if parts[4] in region_total:
            region_total[parts[4]] += amount
        else:
            region_total[parts[4]] = amount
        total += amount
regions = list(region_total.keys())
totals = list(region_total.values())
print(f"总计：{total}")
bar = Bar()
bar.add_xaxis(regions)
bar.add_yaxis("销售额", totals)
bar.render(r"D:\code_work\python-basics\sales_chart.html")
