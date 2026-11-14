import sys

from file_define import JsonFileReader, TextFileReader
from pyecharts.charts import Bar


def pick_reader(path):
    if path.endswith(".json"):
        return JsonFileReader(path)
    return TextFileReader(path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python day49.py <数据文件路径>")
        print("例如: python day49.py python-basics/sales_data.csv")
        sys.exit(1)

    path = sys.argv[1]
    reader = pick_reader(path)
    records = reader.read_data()

    print(f"读到 {len(records)} 条记录")

    region_total = {}
    total = 0

    for r in records:
        amount = r.amount()
        if r.region in region_total:
            region_total[r.region] += amount
        else:
            region_total[r.region] = amount
        total += amount

    for region, value in region_total.items():
        print(region, value)
    print(f"总计: {total}")


    regions = list(region_total.keys())
    totals = list(region_total.values())

    bar = Bar()
    bar.add_xaxis(regions)
    bar.add_yaxis("销售额", totals)
    bar.render("sales_chart.html")