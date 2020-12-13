import tkinter as tk
import mysql.connector as sql

root = tk.Tk()
root.title("Admin Panel")
# root.geometry("900x900")

# establishing connection
def login():
  if username.get() == 'root' and password.get() == 'password':
    global conn
    conn = sql.connect(
      host="localhost",
      user= username.get(),
      passwd= password.get(),
      auth_plugin = 'mysql_native_password',
    )
    if conn.is_connected():
      message = tk.Label(root, text="Connection succesfully made")
      message.grid(row=0, column=1)
      global cursor
      cursor = conn.cursor()
    else:
      message = tk.Label(root, text="Invalid Username/Password")
      message.grid(row=0, column=1)
  else:
    message = tk.Label(root, text="Invalid Username/Password")
    message.grid(row=0, column=1)
  username.delete(0, 'end')
  password.delete(0, 'end')

# labels
username_text = tk.Label(root, text="Username", bg="#333", fg="#fff")
password_text = tk.Label(root, text="Password", bg="#333", fg="#fff")

username_text.grid(row=1, column=1)
password_text.grid(row=2, column=1)

# entries
username = tk.Entry()
password = tk.Entry()

username.grid(row=1, column=2)
password.grid(row=2, column=2)

# buttons
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=3, column=1)

root.mainloop()