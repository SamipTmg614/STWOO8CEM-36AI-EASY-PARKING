from tkinter import *
from tkinter import messagebox
import database

root = Tk()
root.geometry('500x500')
root.maxsize(width = 500 , height=500)
root.minsize(width=500 , height=500)
root.title('parking management')

def register_user():
    database.create_table()
    user= username.get()
    fullname = name.get()
    phone = phone_number.get()
    email = email_id.get()
    passw= passworda.get()
    database.add_user(user,fullname,phone,email,passw)
    root.destroy()
    messagebox.showinfo('success','registered succesfully')
    import main
    

def check_details():
    user = username.get()
    passwa = passworda.get()
    passwb = passwordb.get()
    if passwa == passwb:
        if database.get_user(user,passwa):
            messagebox.showerror('username','username already exists')
        else:
            register_user()
    else:
        messagebox.showerror('error','passwords do not match')
    



Label(root,text='username').place(x=150,y=10)
username = Entry(root,textvariable=StringVar)
username.place(x=220,y=10)


Label(root,text='name').place(x=150,y=30)
name = Entry(root,textvariable=StringVar)
name.place(x=220,y=30)

Label(root,text='phone').place(x=150,y=50)
phone_number = Entry(root,textvariable=StringVar)
phone_number.place(x=220,y=50)

Label(root,text='email').place(x=150,y=70)
email_id = Entry(root,textvariable=StringVar)
email_id.place(x=220,y=70)

Label(root,text='password').place(x=150,y=90)
passworda = Entry(root,textvariable=StringVar)
passworda.place(x=220,y=90)

Label(root,text='re-password').place(x=150,y=110)
passwordb = Entry(root,textvariable=StringVar)
passwordb.place(x=220,y=110)
Button(root,text='signup',command=check_details).place(x=190,y=130)


root.mainloop()

