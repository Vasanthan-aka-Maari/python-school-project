import mysql.connector as sql
import tkinter as tk

# tkinter code
root = tk.Tk()
root.title("Form")
root.geometry("900x900")
root.config(bg="#333")

# function to login and create a hospital database
def login():
  user = username.get()
  passwd = password.get()
  if (user == 'root' and passwd == 'password'):
    db = sql.connect(
      host="localhost",
      user=user,
      passwd=passwd,
      auth_plugin = 'mysql_native_password',
    )
    global cursor
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Hospital")
    cursor.execute("USE Hospital")
    cursor.execute("CREATE TABLE IF NOT EXISTS Patients (patient_name VARCHAR(24), gender ENUM('MALE','FEMALE'), patient_id int PRIMARY KEY AUTO_INCREMENT)")
    if db.is_connected():
      message_label = tk.Label(text="😊 Connection successfully established", bg="#333" ,fg="#54e346")
      message_label.place(x=350, y=100)
  else:
    message_label = tk.Label(text="⚠️ Invalid Username / Password", bg="#333", fg="#E70A2B")
    message_label.place(x=350, y=100)
  username.delete(0, 'end')
  password.delete(0, 'end')

# label
heading = tk.Label(text="Login", bg="#333", fg="#fff", width="500", font=("Ubuntu", 25))
heading.pack()

username_text = tk.Label(text="Username", bg="#333", fg="#fff")
password_text = tk.Label(text="Password", bg="#333", fg="#fff")

username_text.place(x=300, y=200)
password_text.place(x=300, y=300)

# entries
username = tk.Entry()
password = tk.Entry()

username.place(x=400, y=200)
password.place(x=400, y=300)

# button
btn = tk.Button(text="Continue", command=login)
btn.place(x=400, y=400)

root.mainloop()

'''

# cursor to work with db
cursor = db.cursor()

# function to show the table
def show_table():
  cursor.execute("SELECT * FROM Patients")
  print("THE TABLE IS: ")
  for i in cursor:
    print(i)

# function to describe table
def desc_table():
  cursor.execute("DESCRIBE Patients")
  print("DESCRIBING TABLE: ")
  for i in cursor:
    print(i)

# function to reset tabel
def reset_table():
  cursor.execute("RESET TABLE")

# function to add a patient
def add_patient():
  patient_name = input("ENTER THE PATIENT NAME: ")
  age = int(input("ENTER THE PATIENT AGE: "))
  gender = input("ENTER 'M' FOR MALE & 'F' FOR FEMALE: ")
  cursor.execute("INSERT INTO Patients (patient_name, age, gender) VALUES (%s, %s, %s)", (patient_name, age, gender))
  db.commit()
  print(f"Patient {patient_name} has been added successfully.")
  show_table()

# function to delete a record
def delete_patient():
  show_table()
  patient_name = str(input("ENTER THE PATIENT NAME TO REMOVE: "))
  patient_id = int(input("ENTER THE PATIENT ID TO REMOVE: "))
  cursor.execute(f"DELETE FROM Patients WHERE id = {patient_id}")
  db.commit()
  print(f"Patient {patient_name} has been successfully removed.")

# display options to select and execute the appropriate function
print("Enter 1 to adding a patient")
print("Enter 2 to removing a patient")
print("Enter 3 to view table")
print("Enter 4 to describe table")
print("Enter 5 to reset table")

# getting input option from user
option = int(input("Select any one from above: "))

# conditionally executing functions
if option == 1:
  print("Adding a patient")
  add_patient()
elif option == 2:
  print("Removing a patient")
  delete_patient()
elif option == 3:
  show_table()
elif option == 4:
  desc_table()
else:
  print("xxxxxx Invalid Option xxxxxx")

'''

