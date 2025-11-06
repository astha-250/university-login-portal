from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from database import DB_NAME  # make sure database.py is in same folder

def load_student_data(reg_id):
    """Fetch student data from SQLite and show in the table"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT reg_id, name, email, created_at FROM users WHERE reg_id = ?", (reg_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            for i in tree.get_children():
                tree.delete(i)
            tree.insert("", END, values=row)
        else:
            messagebox.showerror("Error", "No student found with this Reg ID.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def back_to_login():
    window.destroy()
    import student_gui  # go back to login window

# ---------------- Dashboard Window ----------------
window = Tk()
window.title("Student Dashboard")
window.geometry("700x500")
window.config(bg="white")

Label(window, text="STUDENT DASHBOARD", font=("Arial", 18, "bold"), bg="white", pady=20).pack()

frame = Frame(window, bg="white")
frame.pack(pady=20)

# Treeview to show student data
columns = ("reg_id", "name", "email", "created_at")
tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col.upper())
    tree.column(col, width=150, anchor=CENTER)

tree.pack(pady=10)

# Example: call this after login with student’s reg ID
# Later you’ll pass the logged-in reg_id dynamically
load_student_data("25BDS0060")  # example student

Button(window, text="BACK TO LOGIN", font=("Arial", 14), command=back_to_login).pack(pady=10)

window.mainloop()
