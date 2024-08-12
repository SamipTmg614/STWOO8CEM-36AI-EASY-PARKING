from tkinter import *
from tkinter import messagebox
import database
import subprocess
import sys

def check():
    if checkvar.get()==1:
        password.config(show='')
    else:
        password.config(show='*')

def submit():
    user = username.get()
    passw = password.get()

    result=database.get_manager(user,passw)
    if result:
        root.destroy()
        subprocess.Popen([sys.executable, 'backend.py'])

    else:
        messagebox.showerror('error','invalid login input')
global root
root = Tk()
  
root.geometry('500x500')
root.maxsize(width = 500 , height=500)
root.minsize(width=500 , height=500)
root.title('parking management')
database.manager_table()

global checkvar
checkvar = IntVar()

Label(root,text='PARKING MANAGER').place(x=200,y=10)

frame = Frame(root,highlightbackground="black",borderwidth=2,width=400,height=400)
frame.place(x=0,y=50)

Label(frame,text='username').place(x=150,y=10)
global username
username = Entry(frame,textvariable=StringVar)
username.place(x=220,y=10)


Label(frame,text='password').place(x=150,y=28)
global password
password = Entry(frame,textvariable=StringVar,show='*')
password.place(x=220,y=28)
c = Checkbutton(frame,text='show password',variable=checkvar,onvalue=1,offvalue=0,height=1,width=20,command=check)
c.place(x=200,y=50)

Button(frame,text='Login',command=submit).place(x=190,y=70)

root.mainloop()
