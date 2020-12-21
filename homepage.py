import tkinter as tk
import mysql.connector as sql
from tkinter import ttk
from tkinter import messagebox
from datetime import *

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
    cursor.execute("CREATE TABLE IF NOT EXISTS Patients (patient_name VARCHAR(24), gender VARCHAR(30), patient_address VARCHAR(50), patient_phone int(20), patient_bloodGroup VARCHAR(20), patient_age int,  patient_status VARCHAR(20), patient_case VARCHAR(50), consultancy_fee int, lab_fee int, treatment_fee int, other_charges int, total int, admit_date VARCHAR(10), patient_id int PRIMARY KEY AUTO_INCREMENT)")
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
    username_text = tk.Label(login_page, text="Username" )
    password_text = tk.Label(login_page, text="Password" )

    username_text.place(x=70, y=100)
    password_text.place(x=70, y=150)

    # entries
    username = tk.Entry(login_page )
    password = tk.Entry(login_page,show='*' )

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
    toplevel.title("Add Patients")

    # functions
    def add_patient():
      admit_date = str(date.today())
      if (p_name.get() and gender_choosen):
        name_value = p_name.get()
        gender_value = str(gender_choosen.get())
        address_value = p_address.get()
        phone_value = int(p_phone.get())
        status_value = str(status_choosen.get())
        bg_value = str(bg_choosen.get())
        age_value = p_age.get()
        case_value = p_case.get()

        cursor.execute("INSERT INTO Patients(patient_name, gender, patient_address, patient_phone, patient_bloodGroup, patient_age, patient_status, patient_case, consultancy_fee, lab_fee, treatment_fee, other_charges, total, admit_date ) VALUES(%s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name_value, gender_value, address_value, phone_value, bg_value, age_value, status_value, case_value, 0, 0, 0, 0, 0, admit_date ))
        conn.commit()

        p_name.delete(0, 'end')
        p_address.delete(0, 'end')
        p_phone.delete(0, 'end')
        bg_choosen.delete(0, 'end')
        status_choosen.delete(0, 'end')
        gender_choosen.delete(0, 'end')
        p_case.delete(0, 'end')
        p_age.delete(0, 'end')


      else:
        messagebox.showwarning("warning", "Please add Patient Name and Patient Gender")

    def quit():
      toplevel.destroy()


    # Combobox creation
    n = tk.StringVar()
    p = tk.StringVar()
    s = tk.StringVar()
    gender_choosen = tk.ttk.Combobox(toplevel, width = 20, textvariable = n,)
    status_choosen = tk.ttk.Combobox(toplevel, width = 20, textvariable = p,)
    bg_choosen = tk.ttk.Combobox(toplevel, width = 20, textvariable = s,)

    # adding values to dropdown
    gender_choosen['values'] = ('MALE', 'FEMALE')
    gender_choosen.grid(row=1, column=1)
    # gender_choosen.current(0)

    status_choosen['values'] = ('In Patient', 'Out Patient', 'Discharge')
    status_choosen.grid(row=7, column=1)
    # status_choosen.current(0)

    bg_choosen['values'] = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
    bg_choosen.grid(row=5, column=1)
    # bg_choosen.current(0)

    # labels
    p_name_label = tk.Label(toplevel, text="Patient Name", width=20, justify=tk.LEFT)
    p_gender_label = tk.Label(toplevel, text="Patient Gender", width=20, justify=tk.LEFT)
    p_age_label = tk.Label(toplevel, text="Patient Age", width=20, justify=tk.LEFT)
    p_phone_label = tk.Label(toplevel, text="Patient Phone", width=20, justify=tk.LEFT)
    p_address_label = tk.Label(toplevel, text="Patient Address", width=20, justify=tk.LEFT)
    p_bg_label = tk.Label(toplevel, text="Patient Blood Group", width=20, justify=tk.LEFT)
    p_case_label = tk.Label(toplevel, text="Patient Disease", width=20, justify=tk.LEFT)
    p_status_label = tk.Label(toplevel, text="Patient Status", width=20, justify=tk.LEFT)

    p_name_label.grid(row=0, column=0, ipady=5, padx=5)
    p_gender_label.grid(row=1, column=0, ipady=5, padx=5)
    p_age_label.grid(row=2, column=0, ipady=5, padx=5)
    p_phone_label.grid(row=3, column=0, ipady=5, padx=5)
    p_address_label.grid(row=4, column=0, ipady=5, padx=5)
    p_bg_label.grid(row=5, column=0, ipady=5, padx=5)
    p_case_label.grid(row=6, column=0, ipady=5, padx=5)
    p_status_label.grid(row=7, column=0, ipady=5, padx=5)


    # entries
    p_name = tk.Entry(toplevel, width=30)
    p_age = tk.Entry(toplevel, width=30)
    p_phone = tk.Entry(toplevel, width=30)
    p_address = tk.Entry(toplevel, width=30)
    p_case = tk.Entry(toplevel, width=30)

    p_name.grid(row=0, column=1, pady=10,  ipadx=5, sticky=tk.NS )
    p_age.grid(row=2, column=1, pady=10,  ipadx=5, sticky=tk.NS )
    p_phone.grid(row=3, column=1, pady=10,  ipadx=5, sticky=tk.NS )
    p_address.grid(row=4, column=1, pady=10,  ipadx=5, sticky=tk.NS )
    p_case.grid(row=6, column=1, pady=10,  ipadx=5, sticky=tk.NS )


    # submit button
    add_patient = tk.Button(toplevel, text="Add", command=add_patient, padx=20)
    add_patient.grid(row=8, column=0)

    quit = tk.Button(toplevel, text="Quit", command=quit, padx=20)
    quit.grid(row=8, column=1)

  else:
    messagebox.showwarning("warning", "Please Login to add Patients")
# function to add patients ends

# function to update patient
def discharge():
  if user:
    toplevel = tk.Toplevel()
    toplevel.title("Update Patient Status")

    # function to remove
    def discharge_patient():
      if id.get():
        query = f"UPDATE Patients SET patient_status = {status_choosen.get()} WHERE patient_id = {id.get()}"
        cursor.execute(query)
        conn.commit()

      else:
        messagebox.showwarning("warning", "Please add a valid Patient ID")

    # label
    label = tk.Label(toplevel, text="Enter Patient ID")
    status_label = tk.Label(toplevel, text="Select Patient Status")

    label.grid(row=0, column=0)
    status_label.grid(row=1, column=0)

    # combobox
    s = tk.StringVar()
    status_choosen = tk.ttk.Combobox(toplevel, width = 20, textvariable = s)

    status_choosen['values'] = ('In Patient', 'Out Patient', 'Discharge')
    status_choosen.grid(row=1, column=1, pady=10)

    # entry
    id = tk.Entry(toplevel)
    id.grid(row=0, column=1, pady=10)

    # button
    button = tk.Button(toplevel, text="Update", padx=15, command=discharge_patient)
    button.grid(row=2, column=1, pady=10)
  else:
    messagebox.showwarning("warning", "Please Login to Remove Patients")
# function to update patient ends

# function to delete table
def delete():
  if user:
    toplevel = tk.Toplevel()
    toplevel.title("Delete Patient")

    # function to select patient
    def delete_patient():
      cursor.execute(f"DELETE FROM Patients WHERE patient_id = {id.get()}")
      conn.commit()
      id.delete(0, 'end')

    # label
    label = tk.Label(toplevel, text="Enter Patient ID")
    label.grid(row=0, column=0, pady=10)

    # entry
    id = tk.Entry(toplevel)
    id.grid(row=0, column=1, pady=10)

    # button
    button = tk.Button(toplevel, text="Delete", padx=15, command=delete_patient)
    button.grid(row=1, column=1, pady=10)

  else:
    messagebox.showwarning("warning", "Please Login to Change Patients Status")
# function to delete table ends

# function to view table
def view():
  if user:
    cursor.execute("SELECT patient_name, gender, patient_case, patient_status, admit_date, patient_id  FROM Patients")
    rows = cursor.fetchall()

    # creating a new frame
    frm = tk.Toplevel(root)
    frm.title("Patients Record")

    # creating a table
    tv = tk.ttk.Treeview(frm, columns=(1,2,3,4,5,6), show="headings", height="5")
    tv.pack()

    # headings
    tv.heading(1, text="Patient Name")
    tv.heading(2, text="Patient Sex")
    tv.heading(3, text="Patient Case")
    tv.heading(4, text="Patient Status")
    tv.heading(5, text="Patient Admit Date")
    tv.heading(6, text="Patient ID")


    # inserting data into table
    for i in rows:
      tv.insert('','end', values=i)

  else:
    messagebox.showwarning("warning", "Please Login to View records")
# function to view table ends

# function to create bill
def bill():
  if user:
    toplevel = tk.Toplevel(root)
    toplevel.title("Add Bill")

    # function to add bill
    def add_bill():
      if (p_id.get()):
        total = int(p_consultancy.get()) + int(p_lab.get()) + int(p_treatment.get()) + int(p_other.get())
        query = f'UPDATE Patients SET consultancy_fee=%s, lab_fee=%s, treatment_fee=%s, other_charges=%s, total=%s WHERE patient_id={p_id.get()}'
        values =(int(p_consultancy.get()), int(p_lab.get()), int(p_treatment.get()),int(p_other.get()), total)

        cursor.execute(query,values)
        conn.commit()

        p_id.delete(0, 'end')
        p_consultancy.delete(0, 'end')
        p_lab.delete(0, 'end')
        p_treatment.delete(0, 'end')
        p_other.delete(0, 'end')
        total=0


      else:
        messagebox.showerror('error', "Please fill out the Entries")

    def close():
      toplevel.destroy()


    # labels
    p_id_label = tk.Label(toplevel, text="Patient ID", width=20, justify=tk.LEFT)
    p_consultancy_label = tk.Label(toplevel, text="Consultancy Fee", width=20, justify=tk.LEFT)
    p_lab_label = tk.Label(toplevel, text="Lab Fee", width=20, justify=tk.LEFT)
    p_treatment_label = tk.Label(toplevel, text="Treatment Fee", width=20, justify=tk.LEFT)
    p_other_label = tk.Label(toplevel, text="Other Charges", width=20, justify=tk.LEFT)

    p_id_label.grid(row=0, column=0, pady=10)
    p_consultancy_label.grid(row=1, column=0, pady=10)
    p_lab_label.grid(row=2, column=0, pady=10)
    p_treatment_label.grid(row=3, column=0, pady=10)
    p_other_label.grid(row=4, column=0, pady=10)

    # entries
    p_id = tk.Entry(toplevel, width=30)
    p_consultancy = tk.Entry(toplevel, width=30)
    p_lab = tk.Entry(toplevel, width=30)
    p_treatment = tk.Entry(toplevel, width=30)
    p_other = tk.Entry(toplevel, width=30)


    p_id.grid(row=0, column=1, pady=10)
    p_consultancy.grid(row=1, column=1, pady=10)
    p_lab.grid(row=2, column=1, pady=10)
    p_treatment.grid(row=3, column=1, pady=10)
    p_other.grid(row=4, column=1, pady=10)

    # button
    button = tk.Button(toplevel, text="Confirm", command=add_bill)
    cancel = tk.Button(toplevel, text="Cancel",command=close)

    button.grid(row=5, column=0, pady=10)
    cancel.grid(row=5, column=1, pady=10)


  else:
    messagebox.showwarning("warning", "Please Login to add Patients")
# function to create bill ends

# function to get id
def get_id():
  if user:
    toplevel = tk.Toplevel(root)

    # label
    label = tk.Label(toplevel, text="Patient ID", width=20)
    label.grid(row=0, column=0, pady=10)

    # entry
    entry = tk.Entry(toplevel)
    entry.grid(row=0, column=1, pady=10)

    button = tk.Button(toplevel, text="Get Reciept", command=lambda: reciept(int(entry.get())), padx=10)
    button.grid(row=1, column=1, pady=10)
  else:
    messagebox.showwarning("warning", "Please Login to add Patients")

# function to get id ends

# function to show reciept
def reciept(id):
  toplevel = tk.Toplevel(root)
  toplevel.title("Reciept")

  query = f"SELECT patient_name, gender, patient_age, patient_phone, consultancy_fee, lab_fee, treatment_fee, other_charges, total FROM Patients  WHERE patient_id={id}"
  cursor.execute(query)

  reciept_values = cursor.fetchall()
  reciept_values = reciept_values[0]
  name = str(reciept_values[0])
  gender = str(reciept_values[1])
  age = str(reciept_values[2])
  phone = str(reciept_values[3])
  c_fee = str(reciept_values[4])
  lab_fee = str(reciept_values[5])
  t_fee = str(reciept_values[6])
  o_charge = str(reciept_values[7])
  total = str(reciept_values[8])

  # labels
  p_name_label = tk.Label(toplevel, text="Patient Name", width=20, justify=tk.LEFT)
  p_gender_label = tk.Label(toplevel, text="Patient Gender", width=20, justify=tk.LEFT)
  p_age_label = tk.Label(toplevel, text="Patient Age", width=20, justify=tk.LEFT)
  p_phone_label = tk.Label(toplevel, text="Patient Phone", width=20, justify=tk.LEFT)
  consultancy_fee_label = tk.Label(toplevel, text="Consultancy Fee", width=20, justify=tk.LEFT)
  lab_fee_label = tk.Label(toplevel, text="Lab Fee", width=20, justify=tk.LEFT)
  treatment_fee_label = tk.Label(toplevel, text="Treatment Fee", width=20, justify=tk.LEFT)
  other_charges_label = tk.Label(toplevel, text="Other charges", width=20, justify=tk.LEFT)
  total_fee_label = tk.Label(toplevel, text="Total Fee", width=20, justify=tk.LEFT)

  p_name_label.grid(row=1, column=0, pady=10)
  p_gender_label.grid(row=2, column=0, pady=10)
  p_age_label.grid(row=3, column=0, pady=10)
  p_phone_label.grid(row=4, column=0, pady=10)
  consultancy_fee_label.grid(row=5, column=0, pady=10)
  lab_fee_label.grid(row=6, column=0, pady=10)
  treatment_fee_label.grid(row=7, column=0, pady=10)
  other_charges_label.grid(row=8, column=0, pady=10)
  total_fee_label.grid(row=9, column=0, pady=10)

  # values
  p_name_value = tk.Label(toplevel, text=name, width=20, justify=tk.LEFT)
  p_gender_value = tk.Label(toplevel, text=gender, width=20, justify=tk.LEFT)
  p_age_value = tk.Label(toplevel, text=age, width=20, justify=tk.LEFT)
  p_phone_value = tk.Label(toplevel, text=phone, width=20, justify=tk.LEFT)
  consultancy_fee_value = tk.Label(toplevel, text=c_fee, width=20, justify=tk.LEFT)
  lab_fee_value = tk.Label(toplevel, text=lab_fee, width=20, justify=tk.LEFT)
  treatment_fee_value = tk.Label(toplevel, text=t_fee, width=20, justify=tk.LEFT)
  other_charges_value = tk.Label(toplevel, text=o_charge, width=20, justify=tk.LEFT)
  total_fee_value = tk.Label(toplevel, text=total, width=20, justify=tk.LEFT)

  p_name_value.grid(row=1, column=1, pady=10)
  p_gender_value.grid(row=2, column=1, pady=10)
  p_age_value.grid(row=3, column=1, pady=10)
  p_phone_value.grid(row=4, column=1, pady=10)
  consultancy_fee_value.grid(row=5, column=1, pady=10)
  lab_fee_value.grid(row=6, column=1, pady=10)
  treatment_fee_value.grid(row=7, column=1, pady=10)
  other_charges_value.grid(row=8, column=1, pady=10)
  total_fee_value.grid(row=9, column=1, pady=10)


# function to show reciept ends

# function to reset table
def reset():
  if user:
    toplevel = tk.Toplevel(root)

    def confirm_reset():
      query="TRUNCATE TABLE Patients"
      cursor.execute(query)
      conn.commit()

    def close_tab():
      toplevel.destroy()

    # label
    label = tk.Label(toplevel, text="Are you sure you want to Reset the table?")
    label.grid(row=0, column=0, pady=10, padx=20)

    # button
    button = tk.Button(toplevel, text="Reset", command=confirm_reset)
    close = tk.Button(toplevel, text="Close", command=close_tab)

    button.grid(row=0, column=1, pady=10)
    close.grid(row=1, column=1, pady=10)

  else :
    messagebox.showerror("error", "Please Login to Reset Table")
# function to reset table ends


# buttons
login = tk.Button(root, text="Login", width=30, pady=10, command=login)
add_patient =  tk.Button(root,text="Admit Patient", width=30, pady=10, command=add)
patient_status =  tk.Button(root,text="Change Status", width=30, pady=10, command=discharge)
view_table =  tk.Button(root,text="Patients Record", width=30, pady=10, command=view)
delete_patient =  tk.Button(root,text="Delete Patient", width=30, pady=10, command=delete)
reset_table =  tk.Button(root,text="Reset Table", width=30, pady=10, command=reset)
create_bill = tk.Button(root, text="Bill", width=30, pady=10, command=bill)
show_reciept = tk.Button(root, text="Show Reciept", width=30, pady=10, command=get_id)

login.grid(row=0, column=0)
add_patient.grid(row=1, column=0)
patient_status.grid(row=2, column=0)
delete_patient.grid(row=3, column=0)
view_table.grid(row=4, column=0)
create_bill.grid(row=5, column=0)
show_reciept.grid(row=6, column=0)
reset_table.grid(row=7, column=0)

root.mainloop()