from tkinter import *
from tkinter import  messagebox
import sqlite3
from database import DB_NAME
def student_login():
    import student_gui

def student_input():
    user = username.get().strip()
    pwd = password.get().strip()
    
    if not user and not pwd:
        messagebox.showwarning("Input Error", "Please enter Username and Password before proceeding.")
        return False
    
    # ✅ Step 2: Verify with database
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE reg_id=? AND password=?", (user, pwd))
    row = cursor.fetchone()
    conn.close()

    if row:
        messagebox.showinfo("Login Successful", f"Welcome, {row[1]}!")
        return True
    else:
        messagebox.showerror("Login Failed", "Invalid Registration ID or Password.")
        return False

    

    
def multi_action():
   if student_input():    # ✅ Only continue if validation passes
        window.destroy()
        student_login()
def Log_out():
    window.destroy()
    import MAINwindow 

window = Tk()

window.geometry("600x500")
window.title("Student's Login Portal")
window.config(background = "white")
label = Label(window,text ='STUDENT PORTAL LOGIN',font=("Arial",16,"bold"),bg = "white",width = 20,height = 2,pady = 30)
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



button = Button(window,text ="Login",command=multi_action,padx = 10)
button.pack()
button_back = Button(window,text="Back",command=Log_out,padx=10)
button_back.pack()
                       
window.mainloop()