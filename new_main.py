from tkinter import *
from tkinter import messagebox
import database
import subprocess,sys
import frontend
from PIL import Image,ImageTk
#Function to open manager interface
def manager_interface():
    win = Toplevel()
    win.geometry('925x500')
    win.configure(bg="#fff")
    win.resizable(False, False)
    win.title('easy parking')
    win.iconbitmap('resources/logo.ico')
    database.manager_table()
    img = PhotoImage(file='resources/loginpage.png',)
    Label(win, image=img, bg='white').pack()

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
            subprocess.Popen([sys.executable, 'backend.py'])
        else:
            messagebox.showerror('error','invalid login input')


    frame = Frame(win,width=350,height=350,bg='#70B6AC')
    frame.place(x=480,y=70)

    heading = Label(frame, text='Sign in', fg='black',bg='#70B6AC', font=('Trebuchet MS', 23))
    heading.place(x=120, y=5)

    def on_enter_username(e):
        username.delete(0, 'end')
    def on_leave_username(e):
        name = username.get()
        if name == '':
            username.insert(0, 'Username')

    # Label(frame,text='username').place(x=150,y=10)
    username = Entry(frame,width=25, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 11),textvariable=StringVar)
    username.place(x=30, y=80)
    username.insert(0, 'Username')
    username.bind('<FocusIn>', on_enter_username)
    username.bind('<FocusOut>', on_leave_username)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter_password(e):
        password.delete(0, 'end')
    def on_leave_password(e):
        name_= password.get()
        if name_== '':
            password.insert(0, 'Password')


    password = Entry(frame, width=25, fg='black', border=0, bg="#70B6AC", font=('Trebuchet MS', 11),textvariable=StringVar,show='*')
    password.place(x=30,y=150)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_enter_password)
    password.bind('<FocusOut>', on_leave_password)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    c = Checkbutton(frame,text='show password',variable=checkvar,onvalue=1,offvalue=0,height=1,width=20,bg='#70B6AC',command=check)
    c.place(x=30,y=200)

    Button(frame, width=39, pady=0, text='LOGIN', bg='black', fg='white', border=1,command=submit).place(x=35,y=230)

    win.mainloop()

    

def customer_interface():#Function to open customer interface
    win = Toplevel()
    win.geometry('925x500')
    win.configure(bg="#fff")
    win.resizable(False, False)
    win.title('easy parking')
    win.iconbitmap('resources/logo.ico')
    img = PhotoImage(file='resources/loginpage.png',)
    Label(win, image=img, bg='white').pack()

    checkvar = IntVar()
    def check():
        if checkvar.get()==1:
            password.config(show='')
        else:
            password.config(show='*')
    def check_password(pa , pb):
        passw = False


        # Check if passwords match
        if pa != pb:
            messagebox.showerror('error', 'Passwords do not match')

        has_digit = False
        has_upper = False
        has_alphabet = False

        if len(pa) >= 8:  #conditions for password to be valid
            for i in pa:
                if i.isdigit():
                    has_digit = True
                if i.isalpha():
                    has_alphabet = True
                if i.isupper():
                    has_upper = True

            if has_digit and has_upper and has_alphabet:
                passw = True
            else:
                messagebox.showerror('error', 'Password must contain at least 1 digit, 1 uppercase letter, and alphabet')
        else:
            messagebox.showerror('error', 'Password must be at least 8 characters long')
        return passw
        

    def submit():#runs when login
        user = username.get()
        passw = password.get()
        database.user_table()
        result=database.get_user(user,passw)
        if result:
            win.destroy()
            root.destroy()
            frontend.frontpage(result)
        else:
            messagebox.showerror('error','invalid login input')

    def signup():
        database.user_table()# makes user table
        win.destroy()
        root.destroy()
        import register

    def forgot_pass():
        ps = Toplevel()
        ps.title('forgot password')
        ps.geometry('300x200')
        ps.configure(bg='#70B6AC')
        Label(ps, text='Enter your username', bg='#70B6AC').pack()
        username = Entry(ps,width=25, fg='black', border=0,bg='white', font=('Trebuchet MS', 11),textvariable=StringVar)
        username.pack()
        Label(ps, text='Enter your phone number', bg='#70B6AC').pack()
        number = Entry(ps,width=25, fg='black', border=0,bg='white', font=('Trebuchet MS', 11),textvariable=StringVar)
        number.pack()
        Label(ps, text='Enter your email', bg='#70B6AC').pack()
        email = Entry(ps,width=25, fg='black', border=0,bg='white', font=('Trebuchet MS', 11),textvariable=StringVar)
        email.pack()

        def changepass(username):
            user = username.get()
            qs = Toplevel()
            qs.title('forgot password')
            qs.geometry('300x200')
            qs.configure(bg='#70B6AC')
            Label(qs, text='Enter your new password', bg='#70B6AC').pack()
            passa = Entry(qs,width=25, fg='black', border=0,bg='white', font=('Trebuchet MS', 11),textvariable=StringVar)
            passa.pack()
            Label(qs, text='ReEnter your new password', bg='#70B6AC').pack()
            passb = Entry(qs,width=25, fg='black', border=0,bg='white', font=('Trebuchet MS', 11),textvariable=StringVar)
            passb.pack()
            def change():
                result = check_password(passa.get(),passb.get())
                if result == True:
                    p=passa.get()
                    
                    conn=database.makeconnection()
                    c=conn.cursor()
                    c.execute("UPDATE users SET password=? WHERE username=?",(p,user))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('success','password changed')
                    qs.destroy()
                else:
                    messagebox.showerror('error','password change failed')

            btn = Button(qs,text='change password',bg='black',fg='white',command=change)
            btn.pack()
        def forgotpass():
            conn=database.makeconnection()
            c=conn.cursor()
            a=username.get()
            b=number.get()
            e=email.get()
            
            c.execute("SELECT * FROM users WHERE username=? AND phone=? AND email=?",(a,b,e))
            det=c.fetchall()
            conn.close()

            if det:
            #    ps.destroy()
               changepass(username)
            else:
                messagebox.showerror('error','invalid infos provided')


        sub = Button(ps,width=20, text='submit', bg='black', fg='white',command=forgotpass)
        sub.pack()
    frame = Frame(win,width=350,height=350,bg='#70B6AC')
    frame.place(x=480,y=70)

    heading = Label(frame, text='Sign in', fg='black',bg='#70B6AC', font=('Trebuchet MS', 23))
    heading.place(x=120, y=5)

    def on_enter_username(e):
        username.delete(0, 'end')
    def on_leave_username(e):
        name = username.get()
        if name == '':
            username.insert(0, 'Username')

    username = Entry(frame,width=25, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 11),textvariable=StringVar)
    username.place(x=30, y=80)
    username.insert(0, 'Username')
    username.bind('<FocusIn>', on_enter_username)
    username.bind('<FocusOut>', on_leave_username)

    
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter_password(e):
        password.delete(0, 'end')
    def on_leave_password(e):
        name_= password.get()
        if name_== '':
            password.insert(0, 'Password')


    password = Entry(frame, width=25, fg='black', border=0, bg="#70B6AC", font=('Trebuchet MS', 11),textvariable=StringVar,show='*')
    password.place(x=30,y=150)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_enter_password)
    password.bind('<FocusOut>', on_leave_password)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    c = Checkbutton(frame,text='show password',variable=checkvar,onvalue=1,offvalue=0,height=1,width=20,bg='#70B6AC',command=check)
    c.place(x=30,y=200)
    Button(frame, width=39, pady=0, text='LOGIN', bg='black', fg='white', border=1,command=submit).place(x=35,y=230)
    Label(frame,text="don't have an account?",bg='#70B6AC', font=('Trebuchet MS', 11,)).place(x=45,y=260)
    Button(frame, width=5,padx=0, pady=0, text='signup', bg='#70B6AC', fg='black', border=0,command=signup).place(x=45,y=280)
    Button(frame, width=20,padx=0, pady=0, text='forgot password', bg='#70B6AC', fg='black', border=0,command=forgot_pass).place(x=190,y=200)

    win.mainloop()                                           

root=Tk()
root.geometry('1920x880')
root.after(10, lambda: root.focus_force())
root.after(10, lambda: root.lift())
root.after(10, lambda: root.attributes('-topmost', True))
root.after(100, lambda: root.attributes('-topmost', False))

home_image=Image.open("resources/homepage.png")
photo=ImageTk.PhotoImage(home_image.resize((1620,880)))
Label(root, image=photo, bg='white').pack()
logo_lbl=Label(text="Car Parking",font=("courier",40,"bold")).pack()#Label for logo

manager_button=Button(text="Manager",font=("courier",30,"bold"),width=11,height=1,bg="black",fg="white",
                      command=manager_interface)#Button to call manager_interface function
manager_button.place(x=210,y=485)

user_button=Button(text="Customer",font=("courier",30,"bold"),width=11,height=1,bg="black",fg="white",
                   command=customer_interface)#Button to call customer_interface function
user_button.place(x=1095,y=485)

root.mainloop()