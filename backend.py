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

root_image = Image.open("resources/clear_bg.jpeg")
root_photo = ImageTk.PhotoImage(root_image.resize((1920, 880)))

canvas = Canvas(root, width=1920, height=880)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=root_photo, anchor="nw")

canvas_var=canvas.create_text(1170,170,text=' ',font=(Font, 40, "bold"), fill=cyan)



logo_image=Image.open("resources/logo.png")
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


def ask_location():
    conn=database.makeconnection()
    c=conn.cursor()
    def on_confirm():
        if code_var.get()==database.fetch_code():
            database.add_location(location_var.get())
            create_location_buttons()
            win.destroy()
        else:
            messagebox.showerror("Alert","Wrong Code",parent=win)
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

    def on_enter_security(e):
        code.delete(0, 'end')
    def on_leave_security(e):
        fetch= code.get()
        if fetch == '':
            code.insert(0, 'security code')

    code_var=StringVar()
    code = Entry(win,width=30, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=code_var)
    code.place(x=30, y=100)

    code.insert(0, 'security code')
    code.bind('<FocusIn>', on_enter_security)
    code.bind('<FocusOut>', on_leave_security)

    confirm_btn=Button(win, text="Submit", bg='#CBFDF1', width=15, font=(Font, 10),activebackground="#CBFDF1",command=on_confirm)
    confirm_btn.place(x=90,y=160)

    win.mainloop()

def update_positions(value,):
    y_start = 60 - int(float(value))# Start position for frames 
    var=0  
    for i, frame in enumerate(frames):           
        new_y = y_start + var*100  # Adjust each frame's y position based on the scale
        if (i+1)%3==0:
            var+=1 
                         
        frame.place_configure(y=new_y)  # Update the frame's position

location_frame=Frame()

frames=[]
Button(text="Add Location",cursor="hand2",bg=cyan,fg=black,font=(Font,10),width=14,command=lambda:ask_location()).place(x=650,y=140)

loc = Frame(root,bg=cyan,height=535,width=600)#slider frame
loc.place(x=50,y=240)

 
def create_location_buttons():
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute("SELECT name FROM location_map")
    location=c.fetchall()
    c.execute("SELECT id FROM location_map")
    location_id=c.fetchall()

    for frame in frames:
        frame.destroy()
    frames.clear()
    
    y_axis=20
    x_axis=30
    ro=1
    co=1

    for i in range(len(location)):
        co+=1
        frame = Frame(loc,bg='#EACF91',height=68,width=150)
        frame.place(x=x_axis,y=y_axis)
        if ro<3:
            ro+=1
            x_axis+=180

        else:
            ro=1
            y_axis+=100
            x_axis=30
            
    
        btn=Button(frame,cursor="hand2",text=location[i],height=3,width=20,background="#AEDCC4",font=(Font,10),command=lambda i=i: backend_funtions.create_button(location_id[i][0], root, canvas, canvas_var))
        btn.place(x=0,y=0)
        

        frames.append(frame)

    scale_float = DoubleVar(value=1)
    scale=Scale(loc,
                    bg='black',command=update_positions,
                    fg='#EACF91',
                    from_ = 0,
                    to = len(location_id)*20,
                    length = 500,
                    orient = VERTICAL,
                    variable=scale_float,
                    )

    scale.place(x=550,y=20)


locations=canvas.create_text(140, 40, text="Locations", font=(Font, 30, "bold"), fill=cyan)
canvas.coords(locations, 400, 180)

database.location_map()
create_location_buttons()

root.mainloop()
