# 计算给定日期是年中的第几天
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def day_of_year(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    day_count = sum(days_in_month[: month - 1]) + day
    return day_count


year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日期:"))
print(f"{year}年{month}月{day}日是这一年的第{day_of_year(year, month, day)}天")