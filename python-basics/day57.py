import pymysql
from config import DB_CONFIG


conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()

cursor.execute("select count(*) from world.city")
print(cursor.fetchone()[0])

cursor.execute(
    "select name, population from world.city order by population desc limit 3"
)
result = cursor.fetchall()
print(result)

for name, pop in result:
    print(name, pop)

cursor.execute(
    "select name, population, continent from world.country where code = 'CHN'"
)
print(cursor.fetchone())

sql = "insert into school.student(name, birth_date, school_no, native_place, identity_card) values (%s, %s, %s, %s, %s)"
cursor.execute(sql, ("测试同学", "2005-01-01", "2025001", "广州", "440100200501010000"))
new_id = cursor.lastrowid 
conn.commit()


def count_cities(conn, code):
    cursor=conn.cursor()
    cursor.execute("select count(*) from world.city where countrycode = %s", (code,))
    result=cursor.fetchone()[0]
    cursor.close()
    return result

print(count_cities(conn, "CHN"))

cursor.execute("delete from school.student where id = %s", (new_id,))
conn.commit()
cursor.execute("delete from school.student where name = '测试同学'")
conn.commit()
print(cursor.rowcount, "行被删除")
conn.close()
