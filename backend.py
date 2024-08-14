from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database,backend_funtions,subprocess,sys


def register_manager():
    def enter_manager():
        database.manager_table()
        conn=database.makeconnection()
        c=conn.cursor()
        c.execute("SELECT id FROM managers")
        manager_list=c.fetchall()

        user=name.get()
        passw=password.get()
        code=security.get()
        conn.close()
           
        exists="FALSE"
        for i in manager_list:
            if user==i[0]:
                exists="TRUE"
                break

        if exists=="FALSE":
            if code==database.fetch_code():
                database.add_manager(user,passw)
                messagebox.showinfo("Parking","New manager sucessfully added!",parent=win)
                win.destroy()
            else:
                messagebox.showerror("Alert","Security code Incorrect!",parent=win)
        else:
            messagebox.showinfo("Alert","Account Already exists",parent=win)
        
    win=Toplevel()
    win.geometry("300x300")
    win.configure(bg='#017A5E')
    Label(win,text="Add Manager",bg='#017A5E',font=(Font,20,'bold'),fg='black').place(x=50,y=10)

    def on_enter_name(e):
        name.delete(0, 'end')
    def on_leave_name(e):
        name_= name.get()
        if name_== '':
            name.insert(0, 'name')
    
    name_var=StringVar()
    name = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=name_var)
    name.place(x=30, y=80)

    name.insert(0, 'name')
    name.bind('<FocusIn>', on_enter_name)
    name.bind('<FocusOut>', on_leave_name)


    def on_enter_password(e):
        password.delete(0, 'end')
    def on_leave_password(e):
        get= password.get()
        if get== '':
            password.insert(0, 'password')

    password_var =StringVar()
    password = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=password_var)
    password.place(x=30, y=120)

    password.insert(0, 'password')
    password.bind('<FocusIn>', on_enter_password)
    password.bind('<FocusOut>', on_leave_password)

    def on_enter_security(e):
        security.delete(0, 'end')
    def on_leave_security(e):
        security_= security.get()
        if security_== '':
            security.insert(0, 'security code')
    
    security_var=StringVar()
    security = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=security_var)
    security.place(x=30, y=160)

    security.insert(0, 'security code')
    security.bind('<FocusIn>', on_enter_security)
    security.bind('<FocusOut>', on_leave_security)

    button = Button(win, text="Submit", bg='#CBFDF1', width=15, font=(Font, 10),activebackground="#CBFDF1",command=enter_manager)
    button.place(x=80, y=220)
    win.mainloop()


def remove_manager():
    def check_manager():
        conn=database.makeconnection()
        c=conn.cursor()

        user=name.get()
        passw=password.get()
        security=code.get()
        c.execute("SELECT id from managers WHERE password=?",(passw,))
        db_user=c.fetchone()
        c.execute("SELECT password from managers WHERE id=?",(user,))
        db_password=c.fetchone()

        if user=="admin":
            messagebox.showerror("Alert","Admin account cannot deleted",parent=win)
        
        elif user.isspace():
            ...
        else:
            if security==database.fetch_code():
                if db_user==None or db_password==None:   
                    messagebox.showinfo("Alert","Username Not Found",parent=win)
                else:
                    database.delete_manager(user)
                    messagebox.showinfo("Success","Manager Removed",parent=win)
                    win.destroy()
            else:
                messagebox.showerror("Alert","Incorrect Security Code!!",parent=win)
        conn.close()

    win=Toplevel()
    win.geometry("300x300")
    win.configure(bg='#017A5E')
    Label(win,text="Remove Manger",bg='#017A5E',font=(Font,20,'bold'),fg='black').place(x=50,y=10)

    def on_enter_Name(e):
        name.delete(0, 'end')
    def on_leave_Name(e):
        name_= name.get()
        if name_== '':
            name.insert(0, 'name')

    Name_var=StringVar()
    name = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=Name_var)
    name.place(x=30, y=80)

    name.insert(0, 'name')
    name.bind('<FocusIn>', on_enter_Name)
    name.bind('<FocusOut>', on_leave_Name)


    def on_enter_passw(e):
        password.delete(0, 'end')
    def on_leave_passw(e):
        get= password.get()
        if get== '':
            password.insert(0, 'password')

    Password_var=StringVar()
    password = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=Password_var)
    password.place(x=30, y=120)

    password.insert(0, 'password')
    password.bind('<FocusIn>', on_enter_passw)
    password.bind('<FocusOut>', on_leave_passw)

    def on_enter_security(e):
        code.delete(0, 'end')
    def on_leave_security(e):
        fetch= code.get()
        if fetch == '':
            code.insert(0, 'security code')

    code_var=StringVar()
    code = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=code_var)
    code.place(x=30, y=160)

    code.insert(0, 'security code')
    code.bind('<FocusIn>', on_enter_security)
    code.bind('<FocusOut>', on_leave_security)

    button = Button(win, text="Submit", bg='#CBFDF1', width=15, font=(Font, 10),activebackground="#CBFDF1",command=check_manager)
    button.place(x=100, y=220)
    win.mainloop()
    
def security_code():
    def on_confirm():   
        confirm_code=current_code.get()
        real_code=database.fetch_code()
        if confirm_code==real_code:
            database.update_code(new_code.get())
            messagebox.showinfo("Alert","Code updated")
            win.destroy()

        else:
            messagebox.showinfo("Alert","Incorrect current code!!")
    win=Toplevel()
    win.geometry("300x300")
    win.configure(bg='#017A5E')
    Label(win,text="Edit Security Code",bg='#017A5E',font=(Font,20,'bold'),fg='black').place(x=40,y=10)

    def on_enter_current(e):
        current_code.delete(0, 'end')
    def on_leave_current(e):
        name = current_code.get()
        if name == '':
            current_code.insert(0, 'current code')

    current_code = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=StringVar)
    current_code.place(x=30, y=80)

    current_code.insert(0, 'current code')
    current_code.bind('<FocusIn>', on_enter_current)
    current_code.bind('<FocusOut>', on_leave_current)


    def on_enter_new(e):
        new_code.delete(0, 'end')
    def on_leave_new(e):
        name = new_code.get()
        if name == '':
            new_code.insert(0, 'new code')

    new_code = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=StringVar)
    new_code.place(x=30, y=120)

    new_code.insert(0, 'new code')
    new_code.bind('<FocusIn>', on_enter_new)
    new_code.bind('<FocusOut>', on_leave_new)

    button = Button(win, text="Submit", bg='#CBFDF1', width=15, font=(Font, 10),activebackground="#CBFDF1",command=on_confirm)
    button.place(x=100, y=180)


    win.mainloop()

def Logout():
    root.destroy()
    import new_main
    subprocess.Popen([sys.executable, 'manager_interface.py'])


  
root=Tk()
root.geometry("1920x880")
cyan="#70B6AC"
black="black"
white="white"
Font="Trebuchet MS"

root_image = Image.open("clear_bg.jpeg")
root_photo = ImageTk.PhotoImage(root_image.resize((1920, 880)))

canvas = Canvas(root, width=1920, height=880)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=root_photo, anchor="nw")


logo_image=Image.open("logo.png")
photo=ImageTk.PhotoImage(logo_image.resize((70,70)))
canvas.create_image(35, 35, image=photo, anchor="nw")

name=canvas.create_text(140, 40, text="Easy Parking", font=(Font, 40, "bold"), fill=cyan)
canvas.coords(name, 270, 65)

Frame(root, width=1920, height=2, bg='white').place(x=0, y=120)
Frame(root, width=2, height=800, bg='white').place(x=800, y=120)

add_manager=Button(text="Add Manager",cursor="hand2",bg=cyan,fg=black,font=(Font,10),width=14,command=register_manager)
add_manager.place(x=1090,y=43)

delete_manager=Button(text="Remove Manager",cursor="hand2",bg=cyan,fg=black,font=(Font,10),width=16,command=remove_manager)
delete_manager.place(x=1203,y=43)

security=Button(text="Security Code",cursor="hand2",bg=cyan,fg=black,font=(Font,10),width=15,command=security_code)
security.place(x=1330,y=43)


logout=Button(text="Logout",cursor="hand2",bg=cyan,fg=black,font=(Font,10),width=8,command=Logout)
logout.place(x=1450,y=43)


def ask_location(button,name_id):
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute(f"SELECT name FROM location_map WHERE id=?",(name_id,))
    given_name=c.fetchone()

    if given_name[0]=="ADD":
        response=messagebox.askyesno("Confirm","Do you want to add a location?")
        if response==1:
            def on_confirm():
                c.execute('''UPDATE location_map
                            SET name=?
                            WHERE id=?''',(location_var.get(),name_id))
                conn.commit()
                conn.close()
                button.config(text=location_var.get())
                backend_funtions.create_button(name_id,root,canvas)
                win.destroy()
            win=Toplevel()
            win.geometry("300x300")
            win.configure(bg='#017A5E')

            def on_enter(e):
                location_name.delete(0, 'end')
            def on_leave(e):
                name = location_var.get()
                if name == '':
                    location_name.insert(0, 'location')


            Label(win,text="Location Name",bg='#017A5E',font=(Font,20,'bold'),fg='black').place(x=60,y=5)
            location_var=StringVar()
            location_name=Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=location_var)
            location_name.insert(0, 'location')
            location_name.bind('<FocusIn>', on_enter)
            location_name.bind('<FocusOut>', on_leave)
            location_name.place(x=30,y=60)

            confirm_btn=Button(win, text="Submit", bg='#CBFDF1', width=15, font=(Font, 10),activebackground="#CBFDF1",command=on_confirm)
            confirm_btn.place(x=90,y=100)

            win.mainloop()
    else:
        backend_funtions.create_button(name_id,root,canvas)
        conn.close()

database.location_map()
conn=database.makeconnection()
c=conn.cursor()
c.execute("SELECT name FROM location_map")
location=c.fetchall()

btn1=Button(root,cursor="hand2",text=location[0],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn1,"Location_1"))
btn1.place(x=30,y=250)

btn2=Button(root,cursor="hand2",text=location[1],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn2,"Location_2"))
btn2.place(x=230,y=250)

btn3=Button(root,cursor="hand2",text=location[2],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn3,"Location_3"))
btn3.place(x=430,y=250)

btn4=Button(root,cursor="hand2",text=location[3],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn4,"Location_4"))
btn4.place(x=630,y=250)

btn5=Button(root,cursor="hand2",text=location[4],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn5,"Location_5"))
btn5.place(x=30,y=330)

btn6=Button(root,cursor="hand2",text=location[5],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn6,"Location_6"))
btn6.place(x=230,y=330)

btn7=Button(root,cursor="hand2",text=location[6],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn7,"Location_7"))
btn7.place(x=430,y=330)

btn8=Button(root,cursor="hand2",text=location[7],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn8,"Location_8"))
btn8.place(x=630,y=330)

btn9=Button(root,cursor="hand2",text=location[8],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn9,"Location_9"))
btn9.place(x=30,y=410)

btn10=Button(root,cursor="hand2",text=location[9],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn10,"Location_10"))
btn10.place(x=230,y=410)

btn11=Button(root,cursor="hand2",text=location[10],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn11,"Location_11"))
btn11.place(x=430,y=410)

btn12=Button(root,cursor="hand2",text=location[11],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn12,"Location_12"))
btn12.place(x=630,y=410)

btn13=Button(root,cursor="hand2",text=location[12],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn13,"Location_13"))
btn13.place(x=30,y=490)

btn14=Button(root,cursor="hand2",text=location[13],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn14,"Location_14"))
btn14.place(x=230,y=490)

btn15=Button(root,cursor="hand2",text=location[14],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn15,"Location_15"))
btn15.place(x=430,y=490)

btn16=Button(root,cursor="hand2",text=location[15],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn16,"Location_16"))
btn16.place(x=630,y=490)

btn17=Button(root,cursor="hand2",text=location[16],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn17,"Location_17"))
btn17.place(x=30,y=570)

btn18=Button(root,cursor="hand2",text=location[17],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn18,"Location_18"))
btn18.place(x=230,y=570)

btn19=Button(root,cursor="hand2",text=location[18],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn19,"Location_19"))
btn19.place(x=430,y=570)

btn20=Button(root,cursor="hand2",text=location[19],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn20,"Location_20"))
btn20.place(x=630,y=570)

btn21=Button(root,cursor="hand2",text=location[20],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn21,"Location_21"))
btn21.place(x=30,y=650)

btn22=Button(root,cursor="hand2",text=location[21],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn22,"Location_22"))
btn22.place(x=230,y=650)

btn23=Button(root,cursor="hand2",text=location[22],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn23,"Location_23"))
btn23.place(x=430,y=650)

btn24=Button(root,cursor="hand2",text=location[23],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda:ask_location(btn24,"Location_24"))
btn24.place(x=630,y=650)

locations=canvas.create_text(140, 40, text="Locations", font=(Font, 30, "bold"), fill=cyan)
canvas.coords(locations, 400, 180)

root.mainloop()