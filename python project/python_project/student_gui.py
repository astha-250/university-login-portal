import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
from database import DB_NAME


def login():
    reg_id=Reg_id_entry.get().strip()   # Get username from Entry field
    #password = password_entry.get()   # Get password from Entry field

    conn = sqlite3.connect(DB_NAME)  # Connect to DB
    cursor = conn.cursor()

    # Parameterized query to check credentials
    cursor.execute("SELECT *,created_at FROM users WHERE reg_id =?", (reg_id,))

    row = cursor.fetchone()  # Fetch one row if exists
    conn.close()

    if row:
        for i in tree.get_children():
            tree.delete(i)
        tree.insert("",tk.END, values=row)    
        
    else:
        messagebox.showinfo("Login Failed", "No student with this reg_id")

# Tkinter GUI setup
root = tk.Tk()
root.title("University Portal Student Lookup")
root.geometry("800x600")

tk.Label(root, text="Enter Reg_id:").pack(pady=5)
Reg_id_entry = tk.Entry(root,width=40)
Reg_id_entry.pack(pady=5)

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

def timetable():
    tt = tk.Toplevel()  # ✅ Or Tk(), but better to use Toplevel for sub-windows
    tt.geometry("1600x1000")
    tt.title("Student Timetable")

    label1 = tk.Label(tt, text='STUDENT TIMETABLE', font=('Arial', 14, "bold"), bg="white", padx=10, pady=10)
    label1.pack()

    timetable_img = tk.PhotoImage(file="C:\\Users\\Astha Jaiswal\\Pictures\\Screenshots\\Screenshot 2025-11-02 210141.png", master=tt)
    label = tk.Label(tt, image=timetable_img)
    label.image = timetable_img  # ✅ Keep a reference!
    label.pack()
    
    tk.Button(tt,text="Close",command=tt.destroy,bg='lightcoral',font=('Arial', 12, 'bold')).pack(pady=10)


def open_courses():
    import courses
    courses.open_courses_window(root)
    
    
tree = ttk.Treeview(root,columns=("reg_id","name","email"), show="headings")
tree.heading("reg_id", text ="Registration ID")
tree.heading("name",text ="Name")
tree.heading("email", text ="Email")
tree.pack(pady=10,fill=tk.X)

Button(root, text="View Courses", command=open_courses,font=("Arial", 14), bg="lightblue").pack(pady=10)

timetable_btn= tk.Button(root,text="View Time Table",command=timetable,font=("Arial", 14), bg="lightblue")
timetable_btn.pack()

tk.Button(root, text="Close", command=root.destroy).pack(pady=5)

root.mainloop()
