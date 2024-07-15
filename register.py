from tkinter import *
from tkinter import messagebox
import database

root = Tk()
root.geometry('1920x1080')
# root.maxsize(width = 1500 , height=900)
# root.minsize(width=1500 , height=900)
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
    


Label(root,text='signup',font=("Regular",48)).place(x=692,y=80)


Label(root,text='username',font=("Regular",30)).place(x=127,y=250)
username = Entry(root,textvariable=StringVar,highlightbackground='black')
username.place(x=159,y=300)


Label(root,text='name',font=("Regular",30)).place(x=529,y=250)
name = Entry(root,textvariable=StringVar)
name.place(x=529,y=300)

Label(root,text='phone',font=("Regular",30)).place(x=529,y=350)
phone_number = Entry(root,textvariable=StringVar)
phone_number.place(x=529,y=400)

Label(root,text='email',font=("Regular",30)).place(x=127,y=350)
email_id = Entry(root,textvariable=StringVar)
email_id.place(x=159,y=400)

Label(root,text='password',font=("Regular",30)).place(x=127,y=450)
passworda = Entry(root,textvariable=StringVar)
passworda.place(x=159,y=500)

Label(root,text='re-password',font=("Regular",20)).place(x=529,y=450)
passwordb = Entry(root,textvariable=StringVar)
passwordb.place(x=529,y=500)
Button(root,text='CREATE ACCOUNT',command=check_details).place(x=127,y=700)


root.mainloop()

