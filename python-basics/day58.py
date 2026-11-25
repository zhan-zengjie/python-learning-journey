import pymysql
from config import DB_CONFIG


def get_conn():
    """返回一个数据库连接"""
    return pymysql.connect(**DB_CONFIG)


def query_all(sql, params=None):
    """查多条，返回元组套元组"""
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()
    finally:
        conn.close()


def query_one(sql, params=None):
    """查一条，没有结果返回 None"""
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchone()
    finally:
        conn.close()


def execute(sql, params=None):
    """增删改，自动提交，返回影响行数"""
    conn=get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql,params)
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()

def main():
    print(
        query_all(
            "select name, population from world.city order by population desc limit 3"
        )
    )
    print(
        query_one(
            "select name, population, continent from world.country where code = 'CHN'"
        )
    )
    execute(
        "insert into school.score(name, cls, score) values (%s, %s, %s)",
        ("李东", "一班", 73),
    )
    print(query_all("select * from school.score where name = '李东'"))
    execute("delete from school.score where name = '李东'")
    print(query_one("select count(*) from school.score"))
    print(execute("delete from school.score where name='不存在的人'"))


if __name__ == "__main__":
    main()
