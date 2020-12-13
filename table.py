import tkinter as tk
from tkinter import ttk
import mysql.connector as sql

conn = sql.connect(
  user="root",
  passwd="password",
  database="Hospital",
  host="localhost",
  auth_plugin="mysql_native_password"
)
cursor = conn.cursor()

select_all = "SELECT * FROM Patients"
cursor.execute(select_all)
rows = cursor.fetchall()

root = tk.Tk()
root.title("Admin Panel")

# frame
frm = tk.Frame(root)
frm.pack(side=tk.LEFT, padx=20)

# table
tv = tk.ttk.Treeview(frm, columns=(1,2,3), show="headings", height='5')
tv.pack()

# headings
tv.heading(1, text="Patient Name")
tv.heading(2, text="Patient Sex")
tv.heading(3, text="Patient ID")

# inserting data into table
for i in rows:
  tv.insert('','end', values=i)

root.mainloop()