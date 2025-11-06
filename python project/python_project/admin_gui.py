
import tkinter as tk
from tkinter import ttk
import sqlite3
from database import DB_NAME

def load_students():
    for i in tree.get_children():
        tree.delete(i)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT reg_id,name,email,created_at FROM users")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

root = tk.Tk()
root.title("Admin Dashboard")
root.geometry("800x500")

tk.Label(root, text="All Students Data", font=("Arial",16,"bold")).pack(pady=10)
tree = ttk.Treeview(root, columns=("reg_id","name","email","created_at"), show="headings")
for col in ("reg_id","name","email","created_at"):
    tree.heading(col, text=col.upper())
    tree.column(col, width=180)
tree.pack(fill=tk.X, padx=10, pady=10)

tk.Button(root, text="Load Data", command=load_students).pack(pady=5)
tk.Button(root, text="Close", command=root.destroy).pack(pady=5)

root.mainloop()

