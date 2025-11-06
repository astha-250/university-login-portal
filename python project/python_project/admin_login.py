from tkinter import *
from tkinter import messagebox
import sqlite3
from database_admin import DB_ADMIN
def admin_login():
    import admin_gui
def admin_input():
    user = username.get().strip()
    pwd = password.get().strip()

    # ✅ Check if fields are empty before proceeding
    if not user or not pwd:
        messagebox.showwarning("Input Error", "Please enter Username and Password before proceeding.")
        return False
    conn = sqlite3.connect(DB_ADMIN)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admins WHERE name=? AND password=?", (user, pwd))
    row = cursor.fetchone()
    conn.close()

    if row:
        messagebox.showinfo("Login Successful", f"Welcome, {row[0]}!")
        return True
    else:
        messagebox.showerror("Login Failed", "Invalid Registration ID or Password.")
        return False

        

def Log_out():
    window.destroy()
    import MAINwindow    
window = Tk()
window.geometry("600x500")
window.title("ADMIN PORTAL LOGIN")
window.config(background = 'white')
#LABEL 1 MAIN TITLE
label = Label(window,text = "ADMIN PORTAL LOGIN",font=("Arial",16,"bold"),width = 20,height = 2,pady = 30,bg = 'white')
label.pack()
#LABEL USERNAME AND A ENTRY BOX
label_username = Label(window,text = 'USERNAME',font=("Arial",14))
username =  Entry(window,font=("Arial",14,"bold"))
label_username.pack()
username.pack()

#LABEL PASSWORD AND A PASSWORD ENTRY BOX
label_password = Label(window,text = 'PASSWORD',font=("Arial",14))
password =  Entry(window,font=("Arial",14,"bold"),show = "*")
label_password.pack()
password.pack()
def multi_action():
   if admin_input(): # ✅ Only continue if validation passes
        window.destroy()
        admin_login()

button_login = Button(window,text = "LOGIN",command = multi_action,padx = 10)
button_login.pack()

button_back = Button(window,text="Back",command=Log_out,padx=10)
button_back.pack()
                       
window.mainloop()                       

                       

