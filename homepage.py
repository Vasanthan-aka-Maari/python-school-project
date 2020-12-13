import tkinter as tk
import mysql.connector as sql
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("1200x600")
root.title("Admin Panel")

# checking for user
user = False

# sql connection
def login_to_db(username, password):
  if (username == 'root' and password == 'password'):
    global conn
    conn = sql.connect(
      host = "localhost",
      user = username,
      passwd = password,
      auth_plugin = 'mysql_native_password',
    )
    if conn.is_connected():
      messagebox.showinfo("success", "Connection has been done!")
      global user
      user = True
    global cursor
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Hospital")
    cursor.execute("USE Hospital")
    cursor.execute("CREATE TABLE IF NOT EXISTS Patients (patient_name VARCHAR(24), gender ENUM('MALE','FEMALE'), patient_id int PRIMARY KEY AUTO_INCREMENT)")
    conn.commit()
  else:
    messagebox.showwarning("warning","Username/password is Invalid")


# function to Login
def login():
  global user
  if user:
    messagebox.showinfo("info", "You are already logged in.")
  else:
    login_page = tk.Toplevel()
    login_page.geometry("400x400")
    login_page.resizable(False, False)
    login_page.title("Login")

    # local login
    def local_login(uname, pword):
      login_to_db(uname, pword)
      username.delete(0, 'end')
      password.delete(0, 'end')
      login_page.destroy()

    # heading
    heading = tk.Label(login_page, text="Login to Database")
    heading.config(font=("Ubuntu",20))
    heading.place(relx = 0.2, rely = 0)

    # labels
    username_text = tk.Label(login_page, text="Username")
    password_text = tk.Label(login_page, text="Password")

    username_text.place(x=70, y=100)
    password_text.place(x=70, y=150)

    # entries
    username = tk.Entry(login_page)
    password = tk.Entry(login_page)

    username.place(x=160, y=100)
    password.place(x=160, y=150)

    # buttons
    login_button = tk.Button(login_page, text="Login", padx=15, command = lambda : local_login(username.get(), password.get()))
    login_button.place(x=170, y=230)
# function to login ends

# function to add patient
def add():
  if user:
    toplevel = tk.Toplevel()

    # functions
    def add_patient():
      if (p_name.get() and gender_choosen.get()):
        name_value = p_name.get()
        gender_value = gender_choosen.get()
        cursor.execute("INSERT INTO Patients(patient_name, gender) VALUES(%s , %s)", (name_value, gender_value))
        p_name.delete(0, 'end')
        gender_choosen.delete(0, 'end')
      else:
        messagebox.showwarning("warning", "Please add Patient Name and Patient Gender")

    def quit():
      toplevel.destroy()

    # Combobox creation
    n = tk.StringVar()
    gender_choosen = tk.ttk.Combobox(toplevel, width = 20, textvariable = n,)

    # adding values to dropdown
    gender_choosen['values'] = ('MALE', 'FEMALE')
    gender_choosen.grid(row=1, column=1)
    gender_choosen.current(0)

    # labels
    p_name_label = tk.Label(toplevel, text="Patient Name", width=20)
    p_gender_label = tk.Label(toplevel, text="Patient Gender", width=20)

    p_name_label.grid(row=0, column=0)
    p_gender_label.grid(row=1, column=0)

    # entries
    p_name = tk.Entry(toplevel, width=30)
    p_name.grid(row=0, column=1)

    # submit button
    add_patient = tk.Button(toplevel, text="Add", command=add_patient, padx=20)
    add_patient.grid(row=3, column=0)

    quit = tk.Button(toplevel, text="Quit", command=quit, padx=20)
    quit.grid(row=3, column=1)

  else:
    messagebox.showwarning("warning", "Please Login to add Patients")
# function to add patients ends

# function to remove patient
def remove():
  if user:
    toplevel = tk.Toplevel()

    # function to remove
    def remove_patient():
      if id.get():
        cursor.execute(f"DELETE FROM Patients WHERE patient_id = {id.get()}")
        id.delete(0, 'end')
      else:
        messagebox.showwarning("warning", "Please add a valid Patient ID")

    # label
    label = tk.Label(toplevel, text="Enter Patient ID")
    label.grid(row=0, column=0)

    # entry
    id = tk.Entry(toplevel)
    id.grid(row=0, column=1)

    # button
    button = tk.Button(toplevel, text="Delete", padx=15, command=remove_patient)
    button.grid(row=1, column=1)
  else:
    messagebox.showwarning("warning", "Please Login to add Patients")
# function to remove patient ends

# function to update table
def update():
  if user:

  else:
    messagebox.showwarning("warning", "Please Login to add Patients")
# function to update table ends

# function to view table
def view():
  if user:
    cursor.execute("SELECT * FROM Patients")
    rows = cursor.fetchall()

    # creating a new frame
    frm = tk.Toplevel(root)

    # creating a table
    tv = tk.ttk.Treeview(frm, columns=(1,2,3), show="headings", height="5")
    tv.pack()

    # headings
    tv.heading(1, text="Patient Name")
    tv.heading(2, text="Patient Sex")
    tv.heading(3, text="Patient ID")

    # inserting data into table
    for i in rows:
      tv.insert('','end', values=i)
      print(i)

  else:
    messagebox.showwarning("warning", "Please Login to add Patients")
# function to view table ends

# buttons
login = tk.Button(root, text="LOGIN", width=30, pady=10, command=login)
add_patient =  tk.Button(root,text="ADD PATIENT", width=30, pady=10, command=add)
delete_patient =  tk.Button(root,text="REMOVE PATIENT", width=30, pady=10, command=remove)
modify_patient =  tk.Button(root,text="MODIFY PATIENT", width=30, pady=10)
view_table =  tk.Button(root,text="VIEW TABLE", width=30, pady=10, command=view)
reset_table =  tk.Button(root,text="RESET TABLE", width=30, pady=10)

login.grid(row=0, column=0)
add_patient.grid(row=1, column=0)
delete_patient.grid(row=2, column=0)
modify_patient.grid(row=3, column=0)
view_table.grid(row=4, column=0)
reset_table.grid(row=5, column=0)

root.mainloop()