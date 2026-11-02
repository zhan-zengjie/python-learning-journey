import json
import os

FILE_NAME = "students.json"
# 读取学生数据
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("数据文件读取失败，将创建新的数据。")

    return {}


# 保存学生数据
def save_data(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# 添加学生
def add_student(students):
    name = input("请输入学生姓名：").strip()

    if not name:
        print("姓名不能为空！")
        return

    if name in students:
        print("该学生已经存在！")
        return

    try:
        score = float(input("请输入学生成绩："))

        if not 0 <= score <= 100:
            print("成绩必须在 0 到 100 之间！")
            return

        students[name] = score
        save_data(students)

        print("添加成功！")

    except ValueError:
        print("成绩必须输入数字！")


# 查询学生
def find_student(students):
    name = input("请输入要查询的学生姓名：").strip()

    if name in students:
        print(f"{name} 的成绩是：{students[name]}")
    else:
        print("没有找到该学生。")


# 显示所有学生
def show_students(students):
    if not students:
        print("目前没有学生数据。")
        return

    print("\n学生成绩列表:")

    for name, score in students.items():
        print(f"姓名：{name}，成绩：{score}")


# 主程序
def main():
    students = load_data()

    while True:
        print("\n====== 学生成绩管理系统 ======")
        print("1. 添加学生")
        print("2. 查询学生")
        print("3. 显示所有学生")
        print("4. 退出程序")

        choice = input("请选择功能：")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            find_student(students)

        elif choice == "3":
            show_students(students)

        elif choice == "4":
            print("程序已退出。")
            break

        else:
            print("输入错误，请重新选择！")


if __name__ == "__main__":
    main()