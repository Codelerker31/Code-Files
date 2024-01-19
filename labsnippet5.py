# import required libraries
import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox


win_log = Tk()
password = None
username = None
cursor = None
name = "users"

# creating connection to mysql database
db = mysql.connect(
    host="127.0.0.1",
    user="root",
    database="employees",
)

cursor = db.cursor()


# login function
def login():
    global win_log, username, password, name, cursor

    # Deleting table if already exists
    cursor.execute(f"DROP TABLE IF EXISTS {name}")
    # Creating Table
    cursor.execute(f"CREATE TABLE {name}(username VARCHAR(255) PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),\
    date_of_birth INT,contact_number INT,password VARCHAR(255),security_question VARCHAR(255),\
    security_question_ans VARCHAR(255))")

    # Inserting values into table
    query1 = f"INSERT INTO {name} VALUES('DL', 'David', 'Leon', '1999-05-20', '2578064', md5('Password'), 'What is your favourite food?', 'Pizza')"
    execSQl(query1)
    db.commit()

    # Altering table, adding column password_hint
    query2 = f"ALTER TABLE {name} ADD COLUMN password_hint VARCHAR(225) NOT NULL"
    execSQl(query2)
    db.commit()

    # Updating table, set password_hint to username
    query3 = f"UPDATE {name} SET password_hint = 'password' WHERE username = '{username}'"
    execSQl(query3)
    db.commit()

    # Altering table, modify required columns to NOT NULL
    query4 = f"ALTER TABLE {name} MODIFY username VARCHAR(255) NOT NULL, MODIFY password VARCHAR(255) NOT NULL,\
     MODIFY password_hint VARCHAR(255) NOT NULL, MODIFY security_question VARCHAR(255) NOT NULL,\
     MODIFY security_question_ans VARCHAR(255) NOT NULL"
    execSQl(query4)
    db.commit()

    # Output
    print("\nThe Table:")
    query5 = f"SELECT * FROM {name}"
    execSQl(query5)

    # Checking if entries are empty
    if username.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter Username And Password", parent=win_log)
    else:
        try:
            # Validating password
            Uname = username.get()
            Pword = password.get()
            cursor.execute(f"SELECT COUNT(1) FROM {name} WHERE username = '{Uname}' and password = md5('{Pword}')")
            count = cursor.fetchall()
            print(count[0][0])

            # Checking password test
            if count[0][0] == 1:
                messagebox.showinfo("Success", "Login Successful", parent=win_log)
            else:
                messagebox.showerror("Login Failed", "Check Password", parent=win_log)
                cursor.execute(f"SELECT security_question FROM users WHERE username = '{Uname}'")
                sec_ques = cursor.fetchall()
                messagebox.showinfo("Security Question", f"{sec_ques[0][0]}", parent=win_log)
                win_log.destroy()
            db.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win_log)


# function prints queries
def execSQl(query):
    global cursor

    cursor.execute(query)
    record = cursor.fetchall()
    print(record)


# login window
def log_win():
    global win_log, username, password

    # app title
    win_log.title("USERS")

    # window size
    win_log.maxsize(width=1920, height=1080)
    win_log.minsize(width=500, height=500)
    win_log.config(bg="#222e50")

    # heading labels
    heading = Label(win_log, text="Login", font='Verdana 25 bold', fg='white', bg='#222e50')
    heading.place(x=80, y=150)

    username_label = Label(win_log, text="Username :", font='Montserrat 11 bold', fg='#fccb06', bg='#222e50')
    username_label.place(x=80, y=220)

    password_label = Label(win_log, text="Password :", font='Montserrat 11 bold', fg='#fccb06', bg='#222e50')
    password_label.place(x=80, y=260)

    # Entry Boxes
    username = StringVar()
    password = StringVar()

    # Username
    username_entry = Entry(win_log, width=40, textvariable=username, bg='#d6d5d2')
    username_entry.place(x=200, y=223)

    # password
    passentry = Entry(win_log, width=40, show="*", textvariable=password, bg='#d6d5d2')
    passentry.place(x=200, y=260)

    # button login

    btn_login = Button(win_log, text="Login", font='Verdana 10 bold', fg='white', bg='#36827f', command=login)
    btn_login.place(x=200, y=293)

    win_log.mainloop()


log_win()