from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import database

root = Tk()
root.geometry('500x500')
root.maxsize(width = 500 , height=500)
root.minsize(width=500 , height=500)
root.title('parking management')


# bg = ImageTk.PhotoImage(Image.open('IMG_5570.JPG'))
# Label(image=bg).grid(row=0,column=0)

checkvar = IntVar()
def check():
    if checkvar.get()==1:
        password.config(show='')
    else:
        password.config(show='*')
def submit():
    user = username.get()
    passw = password.get()
    database.create_table()
    database.get_user(user,passw)
    if database.result:
        messagebox.showinfo('success','login successful')
    else:
        messagebox.showerror('error','invalid login input')

def signup():
    root.destroy()
    import register

Label(root,text='PARKING MANAGER').place(x=200,y=10)

frame = Frame(root,highlightbackground="black",borderwidth=2,width=400,height=400)
frame.place(x=0,y=50)

Label(frame,text='username').place(x=150,y=10)
username = Entry(frame,textvariable=StringVar)
username.place(x=220,y=10)


Label(frame,text='password').place(x=150,y=28)
password = Entry(frame,textvariable=StringVar)
password.place(x=220,y=28)
c = Checkbutton(frame,text='show password',variable=checkvar,onvalue=1,offvalue=0,height=1,width=20,command=check)
c.place(x=200,y=50)

Button(frame,text='Login',command=submit).place(x=190,y=70)
Label(frame,text="Don't have an account?").place(x=150,y=100)

Button(frame,text='Sign up',command=signup).place(x=190,y=130)


root.mainloop()