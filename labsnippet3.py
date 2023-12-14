import mysql.connector as mysql


db = mysql.connect(
    host = "127.0.0.1",
    user = "Adam_sql",
    passwd = "aIlnM2#u&Z1uq7$8^4",
    database = "employees",
)

cursor = db.cursor()

cursor.execute("insert into departments(dept_no, dept_name) values('d102', 'Internal Audit')")

cursor.execute("select * from departments")

RECORDS = cursor.fetchall()

for record in RECORDS:
    print(record)

cursor.execute("insert into departments(dept_no, dept_name) values('d103', 'Health & Safety')")

cursor.execute("update departments set dept_name = 'Health and Safety' where dept_no = 'd103'")

cursor.execute("select * from departments where dept_no= 'd103'")

RECORDS = cursor.fetchall()

for record in RECORDS:
    print(record)

cursor.execute("delete from departments where dept_no= 'd102'")
cursor.execute("delete from departments where dept_no= 'd103'")

cursor.execute("select * from departments")

RECORDS = cursor.fetchall()

for record in RECORDS:
    print(record)

db.close()