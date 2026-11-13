with open(r"D:\code_work\python-basics\sales_data.csv", "r", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        print(line)