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
    passw = data[0][4]
    Label(root,text=user_name, fg='white',bg='black',font=('Trebuchet MS', 23)).place(x=215,y=120,height=23)

    Label(root,text='full_name', fg='black',bg='#70B6AC', font=('Trebuchet MS', 15)).place(x=20,y=170,height=23)
    Label(root,text=full_name, fg='black',bg='#70B6AC',font=('Trebuchet MS', 15)).place(x=150,y=170,height=23)

    Label(root,text='phone number', fg='black',bg='#70B6AC', font=('Trebuchet MS', 15)).place(x=20,y=210,height=23)
    Label(root,text=phone_number, fg='black',bg='#70B6AC',font=('Trebuchet MS', 15)).place(x=150,y=210,height=23)

    Label(root,text='email', fg='black',bg='#70B6AC',font=('Trebuchet MS', 15)).place(x=20,y=250,height=23)
    Label(root,text=email, fg='black',bg='#70B6AC', font=('Trebuchet MS', 15)).place(x=150,y=250,height=23)



    def logout():
        root.destroy()
        subprocess.Popen([sys.executable, 'new_main.py'])

    btn = Button(root,width=20,bg='#325971',text='logout',command=logout)
    btn.place(x=290,y=400,height=37)


    def change_details():
        win = Toplevel(root)
        win.geometry('250x250')
        win.title("change details")
        win.config(bg='#70B6AC')

        label_menu = Label(win, text="Select an option:")
        label_menu.pack(pady=5)

        # Dropdown menu
        options = ["username", "email", "phone",'password']
        selected_option = StringVar(win)
        selected_option.set(options[0])  # Default value

        dropdown = OptionMenu(win, selected_option, *options)
        dropdown.pack(pady=5)

        # Label for entry box
        label_entry = Label(win, text="Enter text:")
        label_entry.pack(pady=5)

        # Entry box
        entry_box = Entry(win)
        entry_box.pack(pady=5)

        def submit():
            chosen_option = selected_option.get()
            entered_text = entry_box.get()
            conn=database.makeconnection()
            c=conn.cursor()
            c.execute(f'''UPDATE users
                    SET {chosen_option}=?
                    WHERE username=? 
                ''',(entered_text,user_name))
            conn.commit()
            conn.close()
            
            data=database.get_user(user_name,passw)
            root.destroy()
            profile_infos(data)


        submit_button = Button(win, text="Submit", command=submit)
        submit_button.pack(pady=10)

        close_button = Button(win, text="Close", command=win.destroy)
        close_button.pack(pady=10)


    Button(root, text="Change details", command=change_details).place(x=20,y=320)


        

    root.mainloop()

# profile_infos([('a','a','a','a')])
