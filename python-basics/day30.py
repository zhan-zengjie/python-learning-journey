# 导入折线图所需的模块
from pyecharts.charts import Line
from pyecharts import options as opts
data = [
    {"month": "1月", "sales": 120},
    {"month": "2月", "sales": 150},
    {"month": "3月", "sales": 135},
    {"month": "4月", "sales": 180},
    {"month": "5月", "sales": 210},
    {"month": "6月", "sales": 190},
    {"month": "7月", "sales": 240},
    {"month": "8月", "sales": 260},
    {"month": "9月", "sales": 230},
    {"month": "10月", "sales": 280},
    {"month": "11月", "sales": 300},
    {"month": "12月", "sales": 350}
]
months = []
sales = []
for item in data:
    months.append(item["month"])
    sales.append(item["sales"])
line = Line()
line.add_xaxis(months)
line.add_yaxis(
    series_name="销售额",  # 数据系列名称
    y_axis=sales,         # 纵坐标数据
    is_smooth=True        # 让折线显示为平滑曲线
)
line.set_global_opts(
    title_opts=opts.TitleOpts(
        title="2026年每月销售额变化"
    ),
    xaxis_opts=opts.AxisOpts(
        name="月份"
    ),
    yaxis_opts=opts.AxisOpts(
        name="销售额（万元）"
    ),
    tooltip_opts=opts.TooltipOpts(
        trigger="axis"
    )
)
line.render("day30_line_chart.html")