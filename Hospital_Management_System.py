import tkinter as tk
from tkinter import messagebox
import sqlite3

db = sqlite3.connect("hospital.db")
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS patients
(name TEXT, age INTEGER, disease TEXT)""")
db.commit()

def add_patient():
    name = e1.get()
    age = e2.get()
    disease = e3.get()

    if not name or not age or not disease:
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        c.execute("INSERT INTO patients VALUES(?,?,?)",
                  (name, int(age), disease))
        db.commit()
        messagebox.showinfo("Success", "Patient Registered!")
        show_patients()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid age")

def show_patients():
    result.delete(0, tk.END)
    for row in c.execute("SELECT * FROM patients"):
        result.insert(tk.END, str(row))

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("400x400")

tk.Label(root, text="HOSPITAL MANAGEMENT SYSTEM",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Patient Name").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Age").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Disease").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Button(root, text="Register Patient",
          command=add_patient).pack(pady=10)

tk.Button(root, text="View Patients",
          command=show_patients).pack()

result = tk.Listbox(root, width=45)
result.pack(pady=10)

root.mainloop()
db.close()
