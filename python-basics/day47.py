with open(r"D:\code_work\python-basics\sales_data.csv", "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    region_total = {}
    all_sales = 0
    for line in f:
        line = line.strip()
        parts = line.split(",")
        sale = int(parts[2]) * int(parts[3])
        if parts[4] in region_total:
            region_total[parts[4]] += sale
        else:
            region_total[parts[4]] = sale
        all_sales += sale
    for region, total in region_total.items():
        print(region, total)
    print(f"总计 {all_sales}")
