from tkinter import *
from tkinter import messagebox
import database
from PIL import Image, ImageTk  # You need to install Pillow library
#import database

def manager_interface():
    win = Toplevel()
    win.geometry('500x500')
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)
    win.title('Parking managment')
    database.manager_table()

    checkvar = IntVar()
    def check():
        if checkvar.get() == 1:
            password.config(show='')
        else:
            password.config(show='*')

    def submit():
        user = username.get()
        passw = password.get()

        result = database.get_manager(user, passw)
        if result:
            win.destroy()
            root.destroy()
            import backend
        else:
            messagebox.showerror('error', 'invalid login input')

    Label(win, text='PARKING MANAGER').place(x=200, y=10)

    frame = Frame(win, highlightbackground="black", borderwidth=2, width=400, height=400)
    frame.place(x=0, y=50)

    Label(frame, text='username').place(x=150, y=10)
    username = Entry(frame, textvariable=StringVar)
    username.place(x=220, y=10)

    Label(frame, text='password').place(x=150, y=28)
    password = Entry(frame, textvariable=StringVar, show='*')
    password.place(x=220, y=28)
    c = Checkbutton(frame, text='show password', variable=checkvar, onvalue=1, offvalue=0, height=1, width=20, command=check)
    c.place(x=200, y=50)

    Button(frame, text='Login', command=submit).place(x=190, y=70)

    win.mainloop()


def customer_interface():
    win = Toplevel()
    win.geometry('500x500')
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)
    win.title('parking management')

    checkvar = IntVar()
    def check():
        if checkvar.get() == 1:
            password.config(show='')
        else:
            password.config(show='*')

    def submit():
        user = username.get()
        passw = password.get()
        database.user_table()
        result = database.get_user(user, passw)
        if result:
            messagebox.showinfo('success', 'login successful')
            win.destroy()
            root.destroy()
        else:
            messagebox.showerror('error', 'invalid login input')

    def signup():
        database.user_table()  # just makes user table
        win.destroy()
        root.destroy()
        import register

    Label(win, text='PARKING SYSTEM').place(x=200, y=10)

    frame = Frame(win, highlightbackground="black", borderwidth=2, width=400, height=400)
    frame.place(x=0, y=50)

    Label(frame, text='username').place(x=150, y=10)
    username = Entry(frame, textvariable=StringVar)
    username.place(x=220, y=10)

    Label(frame, text='password').place(x=150, y=28)
    password = Entry(frame, textvariable=StringVar, show='*')
    password.place(x=220, y=28)
    c = Checkbutton(frame, text='show password', variable=checkvar, onvalue=1, offvalue=0, height=1, width=20, command=check)
    c.place(x=200, y=50)

    Button(frame, text='Login', command=submit).place(x=190, y=70)
    Label(frame, text="Don't have an account?").place(x=150, y=100)

    Button(frame, text='Sign up', command=signup).place(x=190, y=130)

    win.mainloop()


root = Tk()
root.geometry('1920x880')

# Load and display the image
image_path = '/Users/manishakumarishah/Desktop/Back 1.png'
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)

# Create a label to display the image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title label
logo_lbl = Label(root, text="", font=("courier", 40, "bold"), bg="#000000", fg="#00FFFF")
logo_lbl.pack(pady=20)

# Buttons
manager_button = Button(root, text="Manager", font=("courier", 30, "bold"), width=10, height=2, bg="black", fg="Black",command=manager_interface)
manager_button.place(x=150, y=400)

user_button = Button(root, text="Customer", font=("courier", 30, "bold"), width=10, height=2, bg="cyan", fg="Black",command=customer_interface)
user_button.place(x=960, y=400)

root.mainloop()



