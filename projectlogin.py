from tkinter import *
from tkinter import ttk, messagebox
import pymysql

win_log = None
emp_id = None
log_password = None

# ---------------------------------------------------------------Login Function --------------------------------------

# close login function
def close():
    win_log.destroy()

# login window creation function
def open_log():
    global win_log
    win_log = Tk()

def login():
    global win_log, emp_id, log_password

    if emp_id.get() == "" or log_password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win_log)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="payroll management 2")
            cur = con.cursor()

            cur.execute("select * from user_information where emp_id = %s and password = %s",
                        (emp_id.get(), log_password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error ", "Invalid Employee ID And Password", parent=win_log)

            else:
                messagebox.showinfo("Success ", "Successfully Login", parent=win_log)
                close()
                deshboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win_log)


# ---------------------------------------------------------------End Login Function ---------------------------------

# ---------------------------------------------------- Dashboard Panel -----------------------------------------



# -----------------------------------------------------End Dashboard Panel -------------------------------------

# ----------------------------------------------------------- Signup Window ---------------------------------------

# signup window creation function
def signup():
    global win_log
    # close login function
    close()

    # signup database connect
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
        full_name.set('')
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
        NIS_number.set('')
        DoB.set('')

    # start Signup Window
    win = Tk()
    win.title("Payroll Management System")
    win.maxsize(width=1920, height=1080)
    win.minsize(width=500, height=800)
    win.config(bg="#222e50")

    # heading label
    heading = Label(win, text="Signup", font='Verdana 20 bold', fg='red', bg='#222e50')
    heading.pack(pady=30)

    # form data label and entry box
    full_name = StringVar()
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
    NIS_number = IntVar()
    DoB = StringVar()

    frame1 = Frame(win, bg='#222e50')
    frame1.pack(expand=True, fill=BOTH, side=LEFT)

    frame2 = Frame(win, bg='#222e50')
    frame2.pack(expand=True, fill=BOTH, side=LEFT)

    field_1 = {}
    field_2 = {}

    field_1['fullname_label'] = Label(frame1, text="Fullname :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['fullname'] = Entry(frame2, width=40, textvariable=full_name)

    field_1['employee_id_label'] = Label(frame1, text="Employee ID :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['employee_id'] = Entry(frame2, width=40, textvariable=employee_id)

    field_1['address_label'] = Label(frame1, text="Address :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['address'] = Entry(frame2, width=40, textvariable=address)

    field_1['gender_label'] = Label(frame1, text="Gender :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['Radio_button_male'] = ttk.Radiobutton(frame2, text='Male', value="Male", variable=gender)
    field_2['Radio_button_female'] = ttk.Radiobutton(frame2, text='Female', value="Female", variable=gender)

    field_1['space'] = Label(frame1, text=" ", bg='#222e50')

    field_1['department_label'] = Label(frame1, text="Department :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['department'] = Entry(frame2, width=40, textvariable=department)

    field_1['salary_id_label'] = Label(frame1, text="Salary ID :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['salary_id'] = Entry(frame2, width=40, textvariable=salary_id)

    field_1['bank_branch_code_label'] = Label(frame1, text="Bank-Branch Code :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['bank_branch_code'] = Entry(frame2, width=40, textvariable=bank_branch_code)

    field_1['account_no_label'] = Label(frame1, text="Account No. :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['account_no'] = Entry(frame2, width=40, textvariable=account_no)

    field_1['work_hrs_label'] = Label(frame1, text="Work Hours :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['work_hrs'] = Entry(frame2, width=40, textvariable=work_hrs)

    field_1['username_label'] = Label(frame1, text="Username :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['username'] = Entry(frame2, width=40, textvariable=username)

    field_1['NIS_Number_label'] = Label(frame1, text="NIS Number :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['NIS_number'] = Entry(frame2, width=40, textvariable=NIS_number)

    field_1['DOB_label'] = Label(frame1, text="Date of Birth :", font='Verdana 10 bold', fg='white',bg='#222e50')
    field_2['DOB'] = Entry(frame2, width=40, textvariable=DoB)

    field_1['password_label'] = Label(frame1, text="Password :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['password'] = Entry(frame2, width=40, textvariable=password)

    field_1['very_pass_label'] = Label(frame1, text="Verify Password :", font='Verdana 10 bold', fg='white', bg='#222e50')
    field_2['very_pass'] = Entry(frame2, width=40, show="*", textvariable=very_pass)

    for field_1 in field_1.values():
        field_1.focus()
        field_1.pack(pady=8.5, anchor=E)

    for field_2 in field_2.values():
        field_2.focus()
        field_2.pack(pady=10, anchor=CENTER)

    # buttons: signup, clear and switch
    signup_btn = Button(frame2, text="Signup", font='Verdana 10 bold', command=action, fg='white', bg='green')
    signup_btn.pack(padx=5, pady=15, anchor=N, side=LEFT)

    btn_clear = Button(frame2, text="Clear", font='Verdana 10 bold', command=clear, fg='white', bg='red')
    btn_clear.pack(padx=5, pady=15, anchor=N, side=LEFT)

    switch_btn = Button(frame2, text="Switch To Login", command=switch, fg='white', bg='blue')
    switch_btn.pack(padx=5, pady=15, anchor=N, side=LEFT)

    win.mainloop()


# ---------------------------------------------------------------------------End Singup Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------

def log_win():
    global win_log, emp_id, log_password

    # app title
    win_log.title("Payroll Management System")

    # window size and colour
    win_log.maxsize(width=1920, height=1080)
    win_log.minsize(width=500, height=500)
    win_log.config(bg="#222e50")

    # heading label
    heading = Label(win_log, text="Login", font='Verdana 25 bold', fg='green', bg='#222e50')
    heading.pack(pady=50)

    # data label and entry box
    emp_id = IntVar()
    log_password = StringVar()

    log_frame1 = Frame(win_log, bg='#222e50')
    log_frame1.pack(expand=True, fill=BOTH, side=LEFT)

    log_frame2 = Frame(win_log, bg='#222e50')
    log_frame2.pack(expand=True, fill=BOTH, side=LEFT)

    log_field = {}
    log_field_2 = {}

    log_field['emp_id'] = Label(log_frame1, text="Employee ID :", font='Verdana 10 bold', fg='white', bg='#222e50')
    log_field_2['identry'] = Entry(log_frame2, width=40, textvariable=emp_id)

    log_field['userpass'] = Label(log_frame1, text="Password :", font='Verdana 10 bold', fg='white', bg='#222e50')
    log_field_2['passentry'] = Entry(log_frame2, width=40, show="*", textvariable=log_password)

    for log_field in log_field.values():
        log_field.focus()
        log_field.pack(pady=15, anchor=CENTER)

    for log_field_2 in log_field_2.values():
        log_field_2.focus()
        log_field_2.pack(pady=15, anchor=W)

    # buttons: login and register
    btn_login = Button(log_frame2, text="Login", font='Verdana 10 bold', command=login, fg='white', bg='#36827f')
    btn_login.pack(padx=10, pady=5, anchor=N, side=LEFT)

    register_btn = Button(log_frame2, text="Register", font='Verdana 10 bold', command=signup, fg='white', bg='#d4af37')
    register_btn.pack(padx=10, pady=5, anchor=N, side=LEFT)

    win_log.mainloop()


open_log()
log_win()

# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
