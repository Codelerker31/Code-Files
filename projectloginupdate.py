import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import pymysql

# ---------------------------------------------------------------Login Function --------------------------------------
win_log = None
user_id = None
password = None


def close():
    win_log.destroy()


def open_log():
    global win_log
    win_log = Tk()


def login():
    global win_log, user_id, password

    if user_id.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win_log)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="payroll management 2")
            cur = con.cursor()

            cur.execute("select * from user_information where emp_id = %s and password = %s",
                        (user_id.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error ", "Invalid Employee ID And Password", parent=win_log)

            else:
                messagebox.showinfo("Success ", "Successfully Login", parent=win_log)
                close()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win_log)


# ---------------------------------------------------------------End Login Function ---------------------------------

# ---------------------------------------------------- Dashboard Panel -----------------------------------------



# -----------------------------------------------------End Dashboard Panel -------------------------------------

# ----------------------------------------------------------- Signup Window ---------------------------------------

def signup():
    # signup database connect
    global win_log

    close()

    def action():

        if first_name.get() == "" or last_name.get() == "" or address.get() == "" or gender.get() == "" or employee_id.get() == "" \
                or department.get() == "" or username.get() == "" or password.get() == "" or very_pass.get() == "" or \
                bank_branch_code.get() == "" or salary_id.get() == "" or account_no.get() == "" or work_hrs.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=win)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=win)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="payroll management 2")
                cur = con.cursor()
                cur.execute("select * from user_information where username = %s", username.get())
                row = cur.fetchone()
                if row == username.get():
                    messagebox.showerror("Error", "Username Already Exits", parent=win)
                else:
                    cur.execute(
                        "insert into user_information(first_name, last_name, username, emp_id, password,"
                        "address, gender, department, salary_id, bank_branch_code, "
                        "account_number, work_hours) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            username.get(),
                            employee_id.get(),
                            password.get(),
                            address.get(),
                            gender.get(),
                            department.get(),
                            salary_id.get(),
                            bank_branch_code.get(),
                            account_no.get(),
                            work_hrs.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successfull", parent=win)
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)

    # close signup function
    def switch():
        win.destroy()
        open_log()
        log_win()

    # clear data function
    def clear():
        first_name.set('')
        last_name.set('')
        address.set('')
        gender.set("Male")
        employee_id.set('')
        department.set('')
        username.set('')
        password.set('')
        very_pass.set('')
        bank_branch_code.set('')
        salary_id.set('')
        account_no.set('')
        work_hrs.set('')

    # start Signup Window

    win = Tk()
    win.title("Payroll Management System")
    win.maxsize(width=1920, height=1080)
    win.minsize(width=500, height=800)

    bg = PhotoImage(file="—Pngtree—dark vector abstract background_1159556.png")

    # heading label
    heading = Label(win, text="Signup", font='Verdana 20 bold', bg='green')
    heading.pack(ipadx=10, ipady=10)

    background_label = tk.Label(win, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    first_name = StringVar()
    last_name = StringVar()
    address = StringVar()
    gender = StringVar()
    employee_id = IntVar()
    department = StringVar()
    username = StringVar()
    password = StringVar()
    very_pass = StringVar()
    bank_branch_code = IntVar()
    salary_id = IntVar()
    account_no = IntVar()
    work_hrs = IntVar()

    field = {}

    # form data label
    field['first_name_label'] = Label(win, text="First Name :", font='Verdana 10 bold', bg='violet')
    field['first_name'] = Entry(win, width=40, textvariable=first_name, bg='cyan')

    field['last_name_label'] = Label(win, text="Last Name :", font='Verdana 10 bold', bg='violet')
    field['last_name'] = Entry(win, width=40, textvariable=last_name, bg='cyan')

    field['employee_id_label'] = Label(win, text="Employee ID :", font='Verdana 10 bold', bg='violet')
    field['employee_id'] = Entry(win, width=40, textvariable=employee_id, bg='cyan')

    field['address_label'] = Label(win, text="Address :", font='Verdana 10 bold', bg='violet')
    field['address'] = Entry(win, width=40, textvariable=address, bg='cyan')

    field['gender_label'] = Label(win, text="Gender :", font='Verdana 10 bold', bg='violet')
    field['Radio_button_male'] = ttk.Radiobutton(win, text='Male', value="Male", variable=gender)
    field['Radio_button_female'] = ttk.Radiobutton(win, text='Female', value="Female", variable=gender)

    field['department_label'] = Label(win, text="Department :", font='Verdana 10 bold', bg='violet')
    field['department'] = Entry(win, width=40, textvariable=department, bg='cyan')

    field['salary_id_label'] = Label(win, text="Salary ID :", font='Verdana 10 bold', bg='violet')
    field['salary_id'] = Entry(win, width=40, textvariable=salary_id, bg='cyan')

    field['bank_branch_code_label'] = Label(win, text="Bank-Branch Code :", font='Verdana 10 bold', bg='violet')
    field['bank_branch_code'] = Entry(win, width=40, textvariable=bank_branch_code, bg='cyan')

    field['account_no_label'] = Label(win, text="Account No. :", font='Verdana 10 bold', bg='violet')
    field['account_no'] = Entry(win, width=40, textvariable=account_no, bg='cyan')

    field['work_hrs_label'] = Label(win, text="Work Hours :", font='Verdana 10 bold', bg='violet')
    field['work_hrs'] = Entry(win, width=40, textvariable=work_hrs, bg='cyan')

    field['username_label'] = Label(win, text="Username :", font='Verdana 10 bold', bg='violet')
    field['username'] = Entry(win, width=40, textvariable=username, bg='cyan')

    field['password_label'] = Label(win, text="Password :", font='Verdana 10 bold', bg='violet')
    field['password'] = Entry(win, width=40, textvariable=password, bg='cyan')

    field['very_pass_label'] = Label(win, text="Verify Password:", font='Verdana 10 bold', bg='violet')
    field['very_pass'] = Entry(win, width=40, show="*", textvariable=very_pass, bg='cyan')

    for field in field.values():
        field.focus()
        field.pack(padx=1, pady=1, anchor=tk.W)

    register_btn = Button(win, text="Signup", font='Verdana 10 bold', command=action, bg='green')
    register_btn.pack(padx=5, pady=5, side=tk.LEFT)

    btn_clear = Button(win, text="Clear", font='Verdana 10 bold', command=signup, bg='red')
    btn_clear.pack(padx=5, pady=5, side=tk.LEFT)

    switch_btn = Button(win, text="Switch To Login", command=switch, bg='blue')
    switch_btn.pack(padx=5, pady=5, side=tk.LEFT)

    win.mainloop()


# ---------------------------------------------------------------------------End Singup Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------

def log_win():
    global win_log, user_id, password

    # app title
    win_log.title("Payroll Management System")

    # window size
    win_log.maxsize(width=1920, height=1080)
    win_log.minsize(width=500, height=500)
    win_log.config(bg="#222e50")


    # heading labels
    heading = Label(win_log , text = "Login" , font = 'Verdana 25 bold',fg='white',bg='#222e50')
    heading.place(x=80, y=150)

    user_id = Label(win_log, text= "Employee ID :" , font='Montserrat 11 bold',fg='#fccb06',bg='#222e50')
    user_id.place(x=80, y=220)

    password = Label(win_log, text= "Password :" , font='Montserrat 11 bold',fg='#fccb06',bg='#222e50')
    password.place(x=80, y=260)

    #Entry Boxes
    
    user_id = StringVar()
    password = StringVar()

    #ID
    emp_id = Entry(win_log, width=40, textvariable=user_id, bg='#d6d5d2')
    emp_id.focus()
    emp_id.place(x=200, y=223)
    
     #password 
    passentry= Entry(win_log, width=40, show="*", textvariable=password, bg='#d6d5d2')
    passentry.place(x=200, y=260)


    # button login

    btn_login = Button(win_log, text="Login", font='Verdana 10 bold', fg='white', bg='#36827f', command=login)
    btn_login.place(x=200, y=293)

    # signup button

    btn_login = Button(win_log, text="Register",font='Verdana 10 bold', fg='white', bg='#d4af37', command=signup)
    btn_login.place(x=260, y=293)

    win_log.mainloop()


open_log()
log_win()

# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
