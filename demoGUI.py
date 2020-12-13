import tkinter as tk

root = tk.Tk()
root.title("Form")
root.geometry("500x500")
root.config(bg="#333")

heading = tk.Label(text="Login", bg="#333", fg="#fff", width="500", font=("Ubuntu", 25))
heading.pack()


root.mainloop()