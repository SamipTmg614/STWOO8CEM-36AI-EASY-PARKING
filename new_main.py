from tkinter import *
from tkinter import messagebox
import database


#Function to open manager interface
def manager_interface():
    win = Toplevel()
    win.geometry('500x500')
    win.maxsize(width = 500 , height=500)
    win.minsize(width=500 , height=500)
    win.title('parking management')
    database.manager_table()

    checkvar = IntVar()
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
            win.destroy()
            root.destroy()
            import backend
        else:
            messagebox.showerror('error','invalid login input')


    Label(win,text='PARKING MANAGER').place(x=200,y=10)

    frame = Frame(win,highlightbackground="black",borderwidth=2,width=400,height=400)
    frame.place(x=0,y=50)

    Label(frame,text='username').place(x=150,y=10)
    username = Entry(frame,textvariable=StringVar)
    username.place(x=220,y=10)


    Label(frame,text='password').place(x=150,y=28)
    password = Entry(frame,textvariable=StringVar,show='*')
    password.place(x=220,y=28)
    c = Checkbutton(frame,text='show password',variable=checkvar,onvalue=1,offvalue=0,height=1,width=20,command=check)
    c.place(x=200,y=50)

    Button(frame,text='Login',command=submit).place(x=190,y=70)

    win.mainloop()

    

def customer_interface():#Function to open customer interface
    win = Toplevel()
    win.geometry('500x500')
    win.maxsize(width = 500 , height=500)
    win.minsize(width=500 , height=500)
    win.title('parking management')

    checkvar = IntVar()
    def check():
        if checkvar.get()==1:
            password.config(show='')
        else:
            password.config(show='*')
    def submit():
        user = username.get()
        passw = password.get()
        database.user_table()
        result=database.get_user(user,passw)
        if result:
            messagebox.showinfo('success','login successful')
            win.destroy()
            root.destroy()
        else:
            messagebox.showerror('error','invalid login input')

    def signup():
        database.user_table()#just makes user table
        win.destroy()
        root.destroy()
        import register

    Label(win,text='PARKING SYSTEM').place(x=200,y=10)

    frame = Frame(win,highlightbackground="black",borderwidth=2,width=400,height=400)
    frame.place(x=0,y=50)

    Label(frame,text='username').place(x=150,y=10)
    username = Entry(frame,textvariable=StringVar)
    username.place(x=220,y=10)

    Label(frame,text='password').place(x=150,y=28)
    password = Entry(frame,textvariable=StringVar,show='*')
    password.place(x=220,y=28)
    c = Checkbutton(frame,text='show password',variable=checkvar,onvalue=1,offvalue=0,height=1,width=20,command=check)
    c.place(x=200,y=50)

    Button(frame,text='Login',command=submit).place(x=190,y=70)
    Label(frame,text="Don't have an account?").place(x=150,y=100)

    Button(frame,text='Sign up',command=signup).place(x=190,y=130)


    win.mainloop()                                           

root=Tk()
root.geometry('1920x880')

logo_lbl=Label(text="Car Parking",font=("courier",40,"bold")).pack()#Label for logo

manager_button=Button(text="Manager",font=("courier",30,"bold"),width=10,height=2,bg="black",fg="white",
                      command=manager_interface)#Button to call manager_interface function
manager_button.place(x=300,y=350)

user_button=Button(text="Customer",font=("courier",30,"bold"),width=10,height=2,bg="black",fg="white",
                   command=customer_interface)#Button to call customer_interface function
user_button.place(x=950,y=350)

root.mainloop()