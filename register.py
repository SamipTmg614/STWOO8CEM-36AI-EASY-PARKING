from tkinter import *
from tkinter import messagebox
import database
import re
import sys , subprocess
root = Tk()
root.geometry('1545x880')
root.title('parking management')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='resources/REGISTER.png',)
Label(root, image=img, bg='white').pack()

def register_user():
    database.user_table()
    user= username.get()
    fullname = name.get()
    phone = phone_number.get()
    email = email_id.get()
    passw= passworda.get()
    database.add_user(user,fullname,phone,email,passw)
    messagebox.showinfo('success','registered succesfully')
    root.destroy()
    import new_main

def check_password():
    passw = False
    pa = passworda.get()
    pb = passwordb.get()

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
    

def phone():
        valid = NONE
        len_phone=phone_number.get()

        def check_isdigit():
            nonlocal len_phone

            for i in len_phone:
                if i.isdigit():
                    valid = True
                else:
                    valid = False
                    messagebox.showerror('error','phone number is supposed to be digit')
                    break
            return valid
        
        if check_isdigit()== True:
            if len(len_phone)==10:
                        con = database.makeconnection()
                        cursor = con.cursor()
                        cursor.execute("SELECT * FROM users Where phone=?",(phone_number.get(),))
                        result = cursor.fetchall()

                        if result==[]:
                            return  True
                        else:
                            messagebox.showerror('error','phone number is already used')
            else:
                messagebox.showerror('error','phone number should be 10 digit')


def check_email():
    email = email_id.get()
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        messagebox.showerror('Please enter a valid email address.')
        return False
    return True



def check_details():
    database.user_table()
    user = username.get()
    passwa = passworda.get()
    passwb = passwordb.get()

    if phone()==True:
        if check_email()==True:
            if passwa==passwb:
                if check_password() == True:
                    if database.get_user(user,passwa):
                        messagebox.showerror('username','username already exists')
                    else:
                        register_user()
                else:
                    print("error at 97")

            else:
                messagebox.showerror('error','passwords do not match')

heading = Label(root, text='Register user', fg='black',bg='#70B6AC', font=('Trebuchet MS', 23))
heading.place(x=500, y=180)

def on_enter(e):
    username.delete(0, 'end')
def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')

username = Entry(root,width=36,textvariable=StringVar,font=('Trebuchet MS', 11),highlightbackground='black')
username.place(x=267,y=303,height=39)
username.insert(0, 'Username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)




def on_enter(e):
    name.delete(0, 'end')
def on_leave(e):
    fullname = name.get()
    if fullname == '':
        name.insert(0, 'Full Name')

name = Entry(root,width=36,textvariable=StringVar,font=('Trebuchet MS', 11),highlightbackground='black')
name.place(x=267,y=357,height=39)
name.insert(0, 'full name')
name.bind('<FocusIn>', on_enter)
name.bind('<FocusOut>', on_leave)

def on_enter(e):
    phone_number.delete(0, 'end')
def on_leave(e):
    num = phone_number.get()
    if num == '':
        phone_number.insert(0, 'phone number')

phone_number = Entry(root,width=36,textvariable=StringVar,font=('Trebuchet MS', 11),highlightbackground='black')
phone_number.place(x=267,y=411,height=39)
phone_number.insert(0, 'Phone Number')
phone_number.bind('<FocusIn>', on_enter)
phone_number.bind('<FocusOut>', on_leave)



def on_enter(e):
    email_id.delete(0, 'end')
def on_leave(e):
    mail = email_id.get()
    if mail == '':
        email_id.insert(0, 'EMAIL ID')

email_id = Entry(root,width=50,textvariable=StringVar,font=('Trebuchet MS', 11),highlightbackground='black')
email_id.place(x=267,y=465,height=39)
email_id.insert(0, 'EMAIL ID')
email_id.bind('<FocusIn>', on_enter)
email_id.bind('<FocusOut>', on_leave)

def on_enter(e):
    passworda.delete(0, 'end')
def on_leave(e):
    mail = passworda.get()
    if mail == '':
        passworda.insert(0, 'password')

passworda = Entry(root,width=36,textvariable=StringVar,font=('Trebuchet MS', 11),highlightbackground='black')
passworda.place(x=267,y=526,height=39)
passworda.insert(0, 'password')
passworda.bind('<FocusIn>', on_enter)
passworda.bind('<FocusOut>', on_leave)


def on_enter(e):
    passwordb.delete(0, 'end')
def on_leave(e):
    mail = passwordb.get()
    if mail == '':
        passwordb.insert(0, 're-enter password')

passwordb = Entry(root,width=36,textvariable=StringVar,font=('Trebuchet MS', 11),highlightbackground='black')
passwordb.place(x=570,y=526,height=39)
passwordb.insert(0, 're-enter password')
passwordb.bind('<FocusIn>', on_enter)
passwordb.bind('<FocusOut>', on_leave)

Button(root, width=39, pady=0, text='REGISTER', bg='black', fg='white', border=1,command=check_details).place(x=450,y=603)

def back():
    root.destroy()
    subprocess.Popen([sys.executable, 'new_main.py'])

button=Button(root,text='BACK', width=10, pady=0, bg='#70B6AC', fg='black', border=0,command=back)
button.place(x=270,y=660,height=20)

root.mainloop()