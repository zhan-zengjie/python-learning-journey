import pymysql
from day58 import query_all, query_one, execute
from datetime import datetime


def print_students(rows):
    print("ID  姓名  班级  学号  籍贯")
    for id_, name, cls, school_no, native_place in rows:
        print(f"{id_}   {name}  {cls}  {school_no}  {native_place}")


def show_all():
    rows = query_all("select id,name,cls,school_no,native_place from school.student")
    print_students(rows)


def search_by_name(keyword):
    rows = query_all(
        "select id,name,cls,school_no,native_place from school.student where name like %s",
        (f"%{keyword}%",),
    )
    if not rows:
        print("没有找到")
        return
    print_students(rows)


def search_by_cls(cls):
    rows = query_all(
        "select id,name,cls,school_no,native_place from school.student where cls=%s",
        (cls,),
    )
    if not rows:
        print("没有找到")
        return
    print_students(rows)


def add_student():
    name = input("姓名：")
    if not name.strip():
        print("姓名不能为空")
        return
    birth = input("生日(YYYY-MM-DD):")
    try:
        datetime.strptime(birth, "%Y-%m-%d")
    except ValueError:
        print("生日格式不对，请用 YYYY-MM-DD")
        return
    school_no = input("学号:")
    place = input("籍贯:")
    card = input("身份证:")
    cls = input("班级:")
    sql = "insert into school.student(name, birth_date, school_no, native_place, identity_card, cls) values (%s, %s, %s, %s, %s, %s)"
    params = (name, birth, school_no, place, card, cls)
    try:
        execute(sql, params)
        print("添加成功")
    except pymysql.err.IntegrityError:
        print(f"学号 {school_no} 已存在，添加失败")


def update_place_and_cls():
    id_ = input("ID:")
    row = query_one("select * from school.student where id=%s", (id_,))
    if not row:
        print("没有这个学生")
        return
    place = input("新籍贯:")
    cls = input("新班级:")
    print("即将更改：", row)
    execute(
        "update school.student set native_place = %s, cls = %s where id = %s",
        (place, cls, id_),
    )
    print("已更新")


def delete_student():
    id_ = input("要删除的 id:")
    sql = "select * from school.student where id=%s"
    row = query_one(sql, (id_,))
    if not row:
        print("没有这个学生")
        return
    print("即将删除：", row)
    execute("delete from school.student where id=%s", (id_,))
    print("已删除")


def count_by_cls():
    rows = query_all("select cls, count(*) from school.student group by cls")
    for cls, n in rows:
        print(f"{cls}  {n} 人")


def main():
    while True:
        print(
            "\n1.查看全部  2.每班人数  3.按姓名查  4.按班级查  5.添加  6.修改  7.删除  0.退出"
        )
        choice = input("请选择：")
        if choice == "1":
            show_all()
        elif choice == "2":
            count_by_cls()
        elif choice == "3":
            search_by_name(input("姓名关键字："))
        elif choice == "4":
            search_by_cls(input("班级："))
        elif choice == "5":
            add_student()
        elif choice == "6":
            update_place_and_cls()
        elif choice == "7":
            delete_student()
        elif choice == "0":
            break
        else:
            print("没有这个选项")


if __name__ == "__main__":
    main()
