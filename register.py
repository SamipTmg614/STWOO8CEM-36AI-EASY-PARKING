from tkinter import *
from tkinter import messagebox
import database
import re

root = Tk()
root.geometry('1920x880')
root.title('parking management')


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



Label(root,text='signup',font=("Regular",48)).place(x=692,y=80)


Label(root,text='username',font=("Regular",30)).place(x=127,y=250)
username = Entry(root,textvariable=StringVar,highlightbackground='black')
username.place(x=159,y=300)


Label(root,text='name',font=("Regular",30)).place(x=529,y=250)
name = Entry(root,textvariable=StringVar)
name.place(x=529,y=300)

Label(root,text='phone',font=("Regular",30)).place(x=529,y=350)
phone_number = Entry(root,textvariable=IntVar)
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
Button(root,text='Create Account',command=check_details).place(x=127,y=700)

root.mainloop()