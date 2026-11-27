from day58 import query_all, query_one, execute  # ← 直接用你封装好的


def show_all():
    """1. 查看全部"""
    rows = query_all("select id, name, native_place from school.student")
    for id_, name, place in rows:
        print(f"{id_}  {name}  {place}")


def search_by_name(keyword):
    """2. 按姓名模糊查"""
    sql = "select id, name, native_place from school.student where name like %s"
    params = (f"%{keyword}%",)
    rows = query_all(sql, params)
    if not rows:
        print("没有找到")
        return
    for id_, name, place in rows:
        print(f"{id_}  {name}  {place}")


def add_student():
    """3. 添加"""
    name = input("姓名:")
    birth = input("生日(YYYY-MM-DD):")
    no = input("学号:")
    place = input("籍贯:")
    card = input("身份证:")
    sql = "insert into school.student (name, birth_date, school_no, native_place, identity_card) values (%s, %s, %s, %s, %s)"
    n = execute(sql, (name, birth, no, place, card))
    print(f"成功添加 {n} 行")


def update_place():
    """4. 按 id 改籍贯"""
    id_ = input("要改哪个 id:")
    place = input("新籍贯:")
    sql = "update school.student set native_place = %s where id = %s"
    n = execute(sql, (place, id_))
    if n == 0:
        print("没有这个学生")


def delete_student():
    """5. 按 id 删除"""
    id_ = input("要删除的 id:")
    sql="select * from school.student where id=%s"
    row = query_one(sql, (id_,))
    if not row:
        print("没有这个学生")
        return
    print("即将删除：", row)
    execute("delete from school.student where id=%s", (id_,))
    print("已删除")

def main():
    while True:
        print("\n1.查看全部  2.按姓名查  3.添加  4.改籍贯  5.删除  0.退出")
        choice = input("请选择：")
        if choice == "1":
            show_all()
        elif choice == "2":
            search_by_name(input("姓名关键字："))
        elif choice == "3":
            add_student()
        elif choice == "4":
            update_place()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            break
        else:
            print("没有这个选项")


if __name__ == "__main__":
    main()
