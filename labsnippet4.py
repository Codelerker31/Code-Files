# import required libraries
import mysql.connector as mysql


# create table function
def create_table(name):
    # Deleting table if already exists
    cursor.execute(f"DROP TABLE IF EXISTS {name}")
    # Creating Table
    cursor.execute(f"CREATE TABLE {name}(username VARCHAR(255) PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),\
    date_of_birth INT,contact_number INT,password VARCHAR(255),security_question VARCHAR(255),\
    security_question_ans VARCHAR(255))")


# test password function
def test_password(password, username, name):
    # Validating password
    print(f"SELECT COUNT(1) FROM {name} WHERE username = '{username}' and password = md5('{password}')")
    cursor.execute(f"SELECT COUNT(1) FROM {name} WHERE username = '{username}' and password = md5('{password}')")
    count = cursor.fetchall()
    print(count[0][0])

    # Checking password test
    if count[0][0] == 1:
        print("Successful Login")
    else:
        print("Login Failed, check password")
        cursor.execute(f"SELECT security_question FROM users WHERE username = '{username}'")
        sec_ques = cursor.fetchall()
        print(sec_ques[0][0])


# function prints queries
def execSQl(query):
    cursor.execute(query)
    record = cursor.fetchall()
    print(record)


# creating connection to mysql database
db = mysql.connect(
    host="127.0.0.1",
    user="root",
    database="employees",
)

cursor = db.cursor()

name = "users"  # Stating table name
create_table(name)  # Creating table

# Inserting values into table
query1 = f"INSERT INTO {name} VALUES('DL', 'David', 'Leon', '1999-05-20', '2578064', md5('Password'), 'What is your favourite food?', 'Pizza')"
execSQl(query1)
db.commit()

# Output
print("\nThe Table:")
query2 = f"SELECT * FROM {name}"
execSQl(query2)

# Password validation
test_password("password", "DL", name)

db.close()
