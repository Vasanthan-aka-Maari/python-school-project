import tkinter as tk

root = tk.Tk()
root.title("REMOVE PATIENT")

# functions
def remove_patient():
  pass

def quit():
  root.quit()

# labels
p_id_text = tk.Label(text="Patient ID", width=20)

p_id_text.grid(row=0, column=0)

# entries
p_id = tk.Entry(root, width=30)
p_id.grid(row=0, column=1)

# submit button
remove_patient = tk.Button(text="Remove", command=remove_patient, padx=20)
remove_patient.grid(row=3, column=0)

quit = tk.Button(text="Quit", command=quit, padx=20)
quit.grid(row=3, column=1)

root.mainloop()