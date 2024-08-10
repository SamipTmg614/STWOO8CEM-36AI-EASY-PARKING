from tkinter import *
from tkinter import messagebox
import database
import subprocess,sys

def profile_infos(data):
    root = Tk()
    root.geometry('500x500')
    root.title('profile')
    img = PhotoImage(file='resources/profile.png',)
    Label(root, image=img, bg='white').pack()

    user_name = data[0][0]
    full_name = data[0][1]
    phone_number = data[0][2]
    email = data[0][3]

    Label(root,text=user_name).place(x=169,y=129)
    Label(root,text=full_name).place(x=169,y=170)
    Label(root,text=phone_number).place(x=169,y=210)
    Label(root,text=email).place(x=169,y=280)


    def logout():
        root.destroy()
        subprocess.Popen([sys.executable, 'new_main.py'])

    btn = Button(root,width=20,bg='#325971',text='logout',command=logout)
    btn.place(x=290,y=400,height=37)


        

    root.mainloop()