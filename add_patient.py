import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ADD PATIENT")

# functions
def add_patient():
  name = p_name.get()
  gender = gender_choosen.get()
  print(name, gender)
  p_name.delete(0, 'end')
  gender_choosen.delete(0, 'end')

def quit():
  root.quit()

# Combobox creation
n = tk.StringVar()
gender_choosen = tk.ttk.Combobox(root, width = 20, textvariable = n,)

# adding values to dropdown
gender_choosen['values'] = ('MALE', 'FEMALE')
gender_choosen.grid(row=1, column=1)
gender_choosen.current()

# labels
p_name_label = tk.Label(text="Patient Name", width=20)
p_gender_label = tk.Label(text="Patient Gender", width=20)

p_name_label.grid(row=0, column=0)
p_gender_label.grid(row=1, column=0)

# entries
p_name = tk.Entry(root, width=30)
p_name.grid(row=0, column=1)

# submit button
add_patient = tk.Button(text="Add", command=add_patient, padx=20)
add_patient.grid(row=3, column=0)

quit = tk.Button(text="Quit", command=quit, padx=20)
quit.grid(row=3, column=1)

root.mainloop()