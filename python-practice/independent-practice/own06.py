import json
import sys
import pymysql

sys.path.insert(0, r"D:\code_work\python-basics")
from config import DB_CONFIG


def load_students():
    with open("students.json", encoding="utf-8") as f:
        return json.load(f)


def save_to_db(conn, students):
    cursor = conn.cursor()
    cursor.execute("delete from school.score")
    sql = "insert into school.score(name, cls, score) values (%s, %s, %s)"
    for s in students:
        cursor.execute(sql, (s["name"], s["cls"], s["score"]))
    conn.commit()
    cursor.close()


def show_stats(conn):
    cursor = conn.cursor()
    sql = "select cls, count(*), avg(score), max(score), min(score) from school.score group by cls order by avg(score) desc"
    cursor.execute(sql)
    for cls, cnt, avg, mx, mn in cursor.fetchall():
        print(f"{cls} {cnt} 人  平均 {avg:.2f}  最高 {mx}  最低 {mn}")
    cursor.close()


def main():
    conn = pymysql.connect(**DB_CONFIG)
    try:
        students = load_students()
        save_to_db(conn, students)
        show_stats(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
