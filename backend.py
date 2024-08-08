from tkinter import *
from tkinter import messagebox
import datetime
import database
root=Tk()
root.geometry("1920x880")


#Function to change button colour and set values NULL again
def green(button,x,location):
    conn=database.makeconnection()
    c=conn.cursor()
    button.config(text="available",bg="green")
    c.execute(f'''UPDATE {location}
                    SET status=?,model=NULL,number=NULL
                    WHERE id=? 
                  ''',("TRUE",x))
    conn.commit()
    conn.close()
    
#Function to change the button colour and update details ralted to the button
def red(button,x,location):
    conn=database.makeconnection()
    c=conn.cursor()
    button.config(text="booked",bg="red")
    model=model_var.get()
    number=number_var.get()

    c.execute(f'''UPDATE {location}
                    SET status=?,model=?,number=?
                    WHERE id=? 
                ''',("FALSE",model,number,x))
        
    conn.commit()
    conn.close()
   
#Function to check if the slot is available or not
def check_slot(button,x,location):
    database.location_table(location)
    conn=database.makeconnection()
    c=conn.cursor()

    #Code to change the colour and text of the button according to the status
    c.execute(f"SELECT status from {location} WHERE id=?",(x,))
    status=c.fetchone()
    if status[0]=="FALSE":
        win=Toplevel()
        win.geometry("300x300")
        c.execute(f"SELECT model,number FROM {location} WHERE id=?",x)
        details=c.fetchmany()

        detail_label=Label(win,text="Details")
        detail_label.place(x=65,y=0)
        model_label=Label(win,text=f"Model:{details[0][0]}")
        model_label.place(x=0,y=20)
        number_label=Label(win,text=f"Number:{details[0][1]}")
        number_label.place(x=0,y=40)

        c.execute(f"SELECT minute FROM {location} WHERE id=?",(x,))
        minute=c.fetchone()
        c.execute(f"SELECT hour FROM {location} WHERE id=?",(x,))
        hour=c.fetchone()

        time=database.calculate_time(x,location)

        time_label=Label(win,text=f"Entry Time:{hour[0]}:{minute[0]}")
        print(time)
        time_label.place(x=0,y=60)

        conn.close()
        confirm=Button(win,text="Confirm",command=lambda:[green(button,x,location),win.destroy()])
        confirm.place(x=65,y=80)
        win.mainloop()

    elif status[0]=="TRUE":
        win=Toplevel()
        win.geometry("300x300")

        global model_var
        model_var=StringVar()
        model_label=Label(win,text="Model")
        model_label.place(x=10,y=10)
        model_entry=Entry(win,textvariable=model_var)
        model_entry.place(x=60,y=10)

        global number_var
        number_var=StringVar()
        number_label=Label(win,text="Number")
        number_label.place(x=10,y=30)
        number_entry=Entry(win,textvariable=number_var)
        number_entry.place(x=60,y=30)

        t=datetime.datetime.now()
        year=t.year
        month=t.month
        minute=t.minute
        hour=t.hour
        day=t.day
        c.execute(f'''UPDATE {location}
                      SET hour=?, minute=?,year=?,month=?,day=?
                      WHERE id=?''',(hour,minute,year,month,day,x))
        time=str(hour)+":"+str(minute)
        time_label=Label(win,text=f"Time:{time}")
        time_label.place(x=10,y=50)

        conn.commit()
        conn.close()
        submit=Button(win,text="Submit",command=lambda:[red(button,x,location),win.destroy()])
        submit.place(x=80,y=80)
        win.mainloop()

    elif status[0]=="ADD":
        response=messagebox.askyesno("Confirm","Do you want to add a slot?")
        if response==1:
            button.config(text="available",bg="green")
            c.execute(f'''UPDATE {location}
                    SET status=?
                    WHERE id=? 
                ''',("TRUE",x))
            conn.commit()
            conn.close()


#Determines colour of the button according to status in database
def button_status(button,x,location):
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute(f"SELECT status from {location} WHERE id=?",(x,))
    status=c.fetchone()
    if status[0]=="TRUE":
        button.config(text="available",bg="green") 

    elif status[0]=="FALSE":
        button.config(text="booked",bg="red") 

    elif status[0]=="ADD":
        button.config(text="Add",bg="Yellow")
    conn.commit()
    conn.close() 

def register_manager():
    def enter_manager():
        database.manager_table()
        user=username.get()
        passw=password.get()
        database.add_manager(user,passw)
        messagebox.showinfo("Parking","New manager sucessfully added!")
        win.destroy()
    win=Toplevel()
    win.geometry("500x500")
    frame = Frame(win,highlightbackground="black",borderwidth=2,width=400,height=400)
    frame.place(x=0,y=50)

    Label(frame,text='Username').place(x=150,y=10)
    username = Entry(frame,textvariable=StringVar)
    username.place(x=220,y=10)

    Label(frame,text='Password').place(x=150,y=28)
    password = Entry(frame,textvariable=StringVar)
    password.place(x=220,y=28)

    Button(frame,text='Sign up',command=enter_manager).place(x=190,y=130)
    win.mainloop()
    

#Frame for logo
logo=Frame(root,bg="blue",width=30,height=50,borderwidth=4)
logo.pack(fill=X)
add_manager=Button(text="Add Manager",bg="purple",command=register_manager)
add_manager.place(x=1400,y=13)
lbl1=Label(logo,text="test")
lbl1.place(x=600,y=10)

def ask_location(button,name_id):
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute(f"SELECT name FROM location_map WHERE id=?",(name_id,))
    given_name=c.fetchone()

    if given_name[0]=="ADD":
        response=messagebox.askyesno("Confirm","Do you want to add a location?")
        if response==1:
            win=Toplevel()
            win.geometry("300x300")
            location_var=StringVar()
            location_name=Entry(win,textvariable=location_var)
            location_name.pack()
            confirm_btn=Button(win,text="Confirm",command=lambda:on_confirm())
            def on_confirm():
                c.execute('''UPDATE location_map
                            SET name=?
                            WHERE id=?''',(location_var.get(),name_id))
                conn.commit()
                conn.close()
                button.config(text=location_var.get())
                create_button(name_id)
                win.destroy()
            confirm_btn.pack()
            win.mainloop()
    else:
        create_button(name_id)
        conn.close()

def create_button(name_id):
    global spaces

    try:
        spaces.destroy()
    except:
        ...
    location=name_id
    database.location_table(location)
    spaces=Frame(root,width=700,height=880,borderwidth=4,relief=GROOVE)
    spaces.pack(side=RIGHT)
    lbl2=Label(spaces,text="Available Spaces",font=("courier",19,"bold"))
    lbl2.place(x=200)

    #32 Buttons for 32 spaces
    b1=Button(spaces,height=2,width=15,command=lambda:check_slot(b1,"1",location))
    b1.place(x=20,y=120)

    b2=Button(spaces,height=2,width=15,command=lambda:check_slot(b2,"2",location))
    b2.place(x=180,y=120)

    b3=Button(spaces,height=2,width=15,command=lambda:check_slot(b3,"3",location))
    b3.place(x=340,y=120)

    b4=Button(spaces,height=2,width=15,command=lambda:check_slot(b4,"4",location))
    b4.place(x=500,y=120)

    b5=Button(spaces,height=2,width=15,command=lambda:check_slot(b5,"5",location))
    b5.place(x=20,y=200)

    b6=Button(spaces,height=2,width=15,command=lambda:check_slot(b6,"6",location))
    b6.place(x=180,y=200)

    b7=Button(spaces,height=2,width=15,command=lambda:check_slot(b7,"7",location))
    b7.place(x=340,y=200)

    b8=Button(spaces,height=2,width=15,command=lambda:check_slot(b8,"8",location))
    b8.place(x=500,y=200)

    b9=Button(spaces,height=2,width=15,command=lambda:check_slot(b9,"9",location))
    b9.place(x=20,y=280)

    b10=Button(spaces,height=2,width=15,command=lambda:check_slot(b10,"10",location))
    b10.place(x=180,y=280)

    b11=Button(spaces,height=2,width=15,command=lambda:check_slot(b11,"11",location))
    b11.place(x=340,y=280)

    b12=Button(spaces,height=2,width=15,command=lambda:check_slot(b12,"12",location))
    b12.place(x=500,y=280)

    b13=Button(spaces,height=2,width=15,command=lambda:check_slot(b13,"13",location))
    b13.place(x=20,y=360)

    b14=Button(spaces,height=2,width=15,command=lambda:check_slot(b14,"14",location))
    b14.place(x=180,y=360)

    b15=Button(spaces,height=2,width=15,command=lambda:check_slot(b15,"15",location))
    b15.place(x=340,y=360)

    b16=Button(spaces,height=2,width=15,command=lambda:check_slot(b16,"16",location))
    b16.place(x=500,y=360)

    b17=Button(spaces,height=2,width=15,command=lambda:check_slot(b17,"17",location))
    b17.place(x=20,y=440)

    b18=Button(spaces,height=2,width=15,command=lambda:check_slot(b18,"18",location))
    b18.place(x=180,y=440)

    b19=Button(spaces,height=2,width=15,command=lambda:check_slot(b19,"19",location))
    b19.place(x=340,y=440)

    b20=Button(spaces,height=2,width=15,command=lambda:check_slot(b20,"20",location))
    b20.place(x=500,y=440)

    b21=Button(spaces,height=2,width=15,command=lambda:check_slot(b21,"21",location))
    b21.place(x=20,y=520)

    b22=Button(spaces,height=2,width=15,command=lambda:check_slot(b22,"22",location))
    b22.place(x=180,y=520)

    b23=Button(spaces,height=2,width=15,command=lambda:check_slot(b23,"23",location))
    b23.place(x=340,y=520)

    b24=Button(spaces,height=2,width=15,command=lambda:check_slot(b24,"24",location))
    b24.place(x=500,y=520)

    b25=Button(spaces,height=2,width=15,command=lambda:check_slot(b25,"25",location))
    b25.place(x=20,y=600)

    b26=Button(spaces,height=2,width=15,command=lambda:check_slot(b26,"26",location))
    b26.place(x=180,y=600)

    b27=Button(spaces,height=2,width=15,command=lambda:check_slot(b27,"27",location))
    b27.place(x=340,y=600)

    b28=Button(spaces,height=2,width=15,command=lambda:check_slot(b28,"28",location))
    b28.place(x=500,y=600)

    b29=Button(spaces,height=2,width=15,command=lambda:check_slot(b29,"29",location))
    b29.place(x=20,y=680)

    b30=Button(spaces,height=2,width=15,command=lambda:check_slot(b30,"30",location))
    b30.place(x=180,y=680)

    b31=Button(spaces,height=2,width=15,command=lambda:check_slot(b31,"31",location))
    b31.place(x=340,y=680)

    b32=Button(spaces,height=2,width=15,command=lambda:check_slot(b32,"32",location))
    b32.place(x=500,y=680)

    #Mapping the buttons according to status
    button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
                b11,b12,b13,b14,b15,b16,b17,b18,b19,b20
                ,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32]
    i=1
    for ele in button_list:
        button_status(ele,str(i),location)
        i+=1



#Frame for locations
locations=Frame(root,width=900,height=880,relief=GROOVE,borderwidth=4)
locations.pack(side=LEFT)

database.location_map()
conn=database.makeconnection()
c=conn.cursor()
c.execute("SELECT name FROM location_map")
location=c.fetchall()
btn1=Button(locations,text=location[0],height=5,width=30,background="red",command=lambda:ask_location(btn1,"Location_1"))
btn1.place(x=30,y=120)

btn2=Button(locations,text=location[1],height=5,width=30,background="red",command=lambda:ask_location(btn2,"Location_2"))
btn2.place(x=300,y=120)

btn3=Button(locations,text=location[2],height=5,width=30,background="red",command=lambda:ask_location(btn3,"Location_3"))
btn3.place(x=570,y=120)

btn4=Button(locations,text=location[3],height=5,width=30,background="red",command=lambda:ask_location(btn4,"Location_4"))
btn4.place(x=30,y=250)

btn5=Button(locations,text=location[4],height=5,width=30,background="red",command=lambda:ask_location(btn5,"Location_5"))
btn5.place(x=300,y=250)

btn6=Button(locations,text=location[5],height=5,width=30,background="red",command=lambda:ask_location(btn6,"Location_6"))
btn6.place(x=570,y=250)

btn7=Button(locations,text=location[6],height=5,width=30,background="red",command=lambda:ask_location(btn7,"Location_7"))
btn7.place(x=30,y=380)

btn8=Button(locations,text=location[7],height=5,width=30,background="red",command=lambda:ask_location(btn8,"Location_8"))
btn8.place(x=300,y=380)

btn9=Button(locations,text=location[8],height=5,width=30,background="red",command=lambda:ask_location(btn9,"Location_9"))
btn9.place(x=570,y=380)

btn10=Button(locations,text=location[9],height=5,width=30,background="red",command=lambda:ask_location(btn10,"Location_10"))
btn10.place(x=30,y=510)

btn11=Button(locations,text=location[10],height=5,width=30,background="red",command=lambda:ask_location(btn11,"Location_11"))
btn11.place(x=300,y=510)

btn12=Button(locations,text=location[11],height=5,width=30,background="red",command=lambda:ask_location(btn12,"Location_12"))
btn12.place(x=570,y=510)

lbl3=Label(locations,text="Locations",font=("courier",19,"bold"))
lbl3.place(x=350)

root.mainloop()