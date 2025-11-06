from tkinter import *
def open_admin_login():
    import admin_login
def open_student_portal():
    import student_login

window = Tk()

#WINDOW SIZE
window.geometry("600x500")
#TITLE
window.title("Login Portal Main Window")
#icon = PhotoImage(file='C:/Users/satya/Downloads/icon.png.jpeg')
window.config(background = 'white')
#LABEL
label = Label(window,text = 'WELCOME TO UNIVERSITY PORTAL', font=("Arial",16,"bold"),pady = 30,bg ='white')
#BUTTONS
button1 = Button(window,text= 'ADMIN PORTAL',font=("Arial",16,),width=20, height=2, command=open_admin_login,pady = 10)
button2 = Button(window,text = 'STUDENTS PORTAL',font=("Arial",16,),width = 20,height = 2,command = open_student_portal,pady =10)
button3 = Button(window,text = "EXIT",font = ("Arial",16,),width = 20,height = 2,command = window.destroy)
label.pack()
button1.pack()
button2.pack()
button3.pack()

window.mainloop()

