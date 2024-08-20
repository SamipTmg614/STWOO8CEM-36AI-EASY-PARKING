from tkinter import *
import database,datetime
from tkinter import messagebox


def red(button,x,location,win):
    conn=database.makeconnection()
    c=conn.cursor()
    button.config(bg="green",text='')
    c.execute(f'''UPDATE {location}
                    SET status=?,model=NULL,number=NULL
                    WHERE id=? 
                  ''',("TRUE",x))
    win.destroy()
    conn.commit()
    conn.close()
    
#Function to change the button colour and update details ralted to the button
def green(button,x,location,win):
    conn=database.makeconnection()
    c=conn.cursor()
    model=model_var.get()
    number=number_var.get()

    if model!='' and number!='':
        button.config(bg="red",text='')
        c.execute(f'''UPDATE {location}
                        SET status=?,model=?,number=?
                        WHERE id=? 
                    ''',("FALSE",model,number,x))
        win.destroy()    
        conn.commit()
        conn.close()

    else:
        messagebox.showinfo("Alert","Information Empty",parent=win)

def check_slot(button,x,location):
    database.location_table(location)
    conn=database.makeconnection()
    c=conn.cursor()
    win=Toplevel()
    win.geometry("300x300")
    win.configure(bg='#017A5E')
    win.title("Easy Parking")

    #Code to change the colour and text of the button according to the status
    c.execute(f"SELECT status from {location} WHERE id=?",(x,))
    status=c.fetchone()
    if status[0]=="TRUE":
        Label(win,text="Details",bg='#017A5E',font=('Trebuchet MS',20,'bold'),fg='black').place(x=100,y=10)
        global model_var
        model_var = Entry(win,width=23, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=StringVar)

        def on_enter(e):
            model_var.delete(0, 'end')
        def on_leave(e):
            name = model_var.get()
            if name == '':
                model_var.insert(0, 'model')

        model_var.place(x=30, y=80)
        model_var.insert(0, 'model')
        model_var.bind('<FocusIn>', on_enter)
        model_var.bind('<FocusOut>', on_leave)

        global number_var
        number_var = Entry(win,width=23, fg='black', border=0,bg='#70B6AC', font=('Trebuchet MS', 12),textvariable=StringVar)
        def on_enter(e):
            number_var.delete(0, 'end')
        def on_leave(e):
            name = number_var.get()
            if name == '':
                number_var.insert(0, 'number')

        number_var.place(x=30, y=120)
        number_var.insert(0, 'number')
        number_var.bind('<FocusIn>', on_enter)
        number_var.bind('<FocusOut>', on_leave)
        t=datetime.datetime.now()
        year=t.year
        month=t.month
        minute=t.minute
        hour=t.hour
        day=t.day
        c.execute(f'''UPDATE {location}
                      SET hour=?, minute=?,year=?,month=?,day=?
                      WHERE id=?''',(hour,minute,year,month,day,x))
        conn.close()
        time=str(hour)+":"+str(minute)
        Label(win,text=f"Entry Time:{time}",bg='#017A5E',font=('Trebuchet MS',12),fg='black').place(x=30,y=150)
        Button(win, text="Submit", bg='#CBFDF1', width=15, font=('Trebuchet MS', 10),activebackground="#CBFDF1",
               command=lambda:[green(button,x,location,win)]).place(x=80, y=180)
        win.mainloop()

    elif status[0]=="FALSE":
        c.execute(f"SELECT model,number FROM {location} WHERE id=?",(x,))
        details=c.fetchmany()

        Label(win,text="Details",bg='#017A5E',font=('Trebuchet MS',20,'bold'),fg='black').place(x=100,y=5)
        Label(win,text=f"Model:{details[0][0]}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=60)
        Label(win,text=f"Number:{details[0][1]}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=85)

        c.execute(f"SELECT minute FROM {location} WHERE id=?",(x,))
        minute=c.fetchone()
        c.execute(f"SELECT hour FROM {location} WHERE id=?",(x,))
        hour=c.fetchone()
        conn.close()
        price=database.calculate_amt(x,location)
        time_label=f"{hour[0]}:{minute[0]}"
        Label(win,text=f"Entry Time:{time_label}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=110)
        Label(win,text=f"Price:{price}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=135)
        submit= Button(win, text="Submit", bg='#CBFDF1', width=15, font=('Trebuchet MS', 10),activebackground="#CBFDF1"
                       ,command=lambda:[red(button,x,location,win)])
        submit.place(x=80,y=165)
        win.mainloop()

def button_status(button,x,location):
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute(f"SELECT status from {location} WHERE id=?",(x,))
    status=c.fetchone()

    if status[0]=="TRUE":
        button.config(bg="green") 

    elif status[0]=="FALSE":
        button.config(bg="red") 

    conn.close() 


frames=[]

def update_positions_slots(value,):
    y_start = 60 - int(float(value))*50# Start position for frames 
    var=0  
    for i, frame in enumerate(frames):           
        new_y = y_start + var*50  # Adjust each frame's y position based on the scale
        if (i+1)%9==0:
            var+=1 
                         
        frame.place_configure(y=new_y)  # Update the frame's position

def create_button(name_id,root,canvas,canvas_var):
    conn=database.makeconnection()
    database.location_table((name_id))
    c=conn.cursor()
    c.execute("SELECT name FROM location_map WHERE id=?",(name_id,))
    name=c.fetchone()

    c.execute(f"SELECT id from {name_id}")
    button_length=c.fetchall()

    conn.close()
    def slot():
        database.add_slot((len(button_length)+1),name_id)
        create_button(name_id,root,canvas,canvas_var)
    cyan="#70B6AC"
    Button(text="Add Slot",cursor="hand2",bg=cyan,fg="black",font=("Trebuchet MS",10),width=14,command=slot).place(x=1400,y=140)

    loc = Frame(root,bg=cyan,height=535,width=600)#slider frame
    loc.place(x=850,y=240)

    location=name_id
    database.location_table(location)

    for frame in frames:
        frame.destroy()
    frames.clear()
    
    scale_float = DoubleVar(value=1)
    scale=Scale(loc,
                    bg='black',command=update_positions_slots,
                    fg='#EACF91',
                    from_ = 0,
                    to = len(button_length)//8,
                    length = 500,
                    orient = VERTICAL,
                    variable=scale_float,
                    )

    scale.place(x=550,y=20)
    canvas.itemconfig(canvas_var,text=f"{name[0]}")

    y_axis=20
    x_axis=30
    ro=1
    co=1

    for i in range(1,len(button_length)+1):
        co+=1
        frame = Frame(loc,bg=cyan,height=68,width=50)
        frame.place(x=x_axis,y=y_axis)
        if ro<9:
            ro+=1
            x_axis+=50

        else:
            ro=1
            y_axis+=50
            x_axis=30
            
        button=Button(frame,height=1,width=5,cursor="hand2")
        button.config(command=lambda button=button,i=i:check_slot(button,str(i),location))
        frames.append(frame)
        button.pack()
        button_status(button,str(i),location)

    conn.close()