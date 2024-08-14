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

    #Code to change the colour and text of the button according to the status
    c.execute(f"SELECT status from {location} WHERE id=?",(x,))
    status=c.fetchone()
    if status[0]=="FALSE":
        win=Toplevel()
        win.geometry("300x300")
        win.configure(bg='#017A5E')
        c.execute(f"SELECT model,number FROM {location} WHERE id=?",(x,))
        details=c.fetchmany()

        Label(win,text="Details",bg='#017A5E',font=('Trebuchet MS',20,'bold'),fg='black').place(x=100,y=5)
        Label(win,text=f"Model:{details[0][0]}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=60)
        Label(win,text=f"Number:{details[0][1]}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=85)

        c.execute(f"SELECT minute FROM {location} WHERE id=?",(x,))
        minute=c.fetchone()
        c.execute(f"SELECT hour FROM {location} WHERE id=?",(x,))
        hour=c.fetchone()

        price=database.calculate_time(x,location)
        time_label=f"{hour[0]}:{minute[0]}"
        Label(win,text=f"Entry Time:{time_label}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=110)
        Label(win,text=f"Price:{price}",bg='#70B6AC',width=23,font=('Trebuchet MS',12),fg='black').place(x=40,y=135)
        conn.close()

        submit= Button(win, text="Submit", bg='#CBFDF1', width=15, font=('Trebuchet MS', 10),activebackground="#CBFDF1",command=lambda:[red(button,x,location,win)])
        submit.place(x=80,y=165)
        win.mainloop()

    elif status[0]=="TRUE":
        win=Toplevel()
        win.geometry("300x300")
        win.configure(bg='#017A5E')
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
        time=str(hour)+":"+str(minute)
        Label(win,text=f"Entry Time:{time}",bg='#017A5E',font=('Trebuchet MS',12),fg='black').place(x=30,y=150)

        conn.commit()
        conn.close()
        Button(win, text="Submit", bg='#CBFDF1', width=15, font=('Trebuchet MS', 10),activebackground="#CBFDF1",command=lambda:[green(button,x,location,win)]).place(x=80, y=180)
        win.mainloop()

    elif status[0]=="ADD":
        button.config(bg="green",text='')
        c.execute(f'''UPDATE {location}
                SET status=?
                WHERE id=? 
            ''',("TRUE",x))
        conn.commit()
        conn.close()

def button_status(button,x,location):
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute(f"SELECT status from {location} WHERE id=?",(x,))
    status=c.fetchone()

    if status[0]=="TRUE":
        button.config(bg="green") 

    elif status[0]=="FALSE":
        button.config(bg="red") 

    else:
        button.config(text="Add",bg="#cbfdf1")
    conn.close() 

def create_button(name_id,root,canvas):
    cyan="#70B6AC"
    Font="Trebuchet MS"
    location=name_id
    database.location_table(location)
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute("SELECT name FROM location_map WHERE id=?",(location,))
    name=c.fetchone()
    name=canvas.create_text(140, 40, text=f"{name[0]}", font=(Font, 40, "bold"), fill=cyan)
    canvas.coords(name, 1170, 180)

    #32 Buttons for 32 root
    b1=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b1,"1",location))
    b1.place(x=830,y=250)

    b2=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b2,"2",location))
    b2.place(x=910,y=250)

    b3=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b3,"3",location))
    b3.place(x=990,y=250)

    b4=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b4,"4",location))
    b4.place(x=1070,y=250)

    b5=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b5,"5",location))
    b5.place(x=1150,y=250)

    b6=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b6,"6",location))
    b6.place(x=1230,y=250)

    b7=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b7,"7",location))
    b7.place(x=1310,y=250)

    b8=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b8,"8",location))
    b8.place(x=1390,y=250)

    b9=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b9,"9",location))
    b9.place(x=1470,y=250)

    b10=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b10,"10",location))
    b10.place(x=830,y=300)

    b11=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b11,"11",location))
    b11.place(x=910,y=300)

    b12=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b12,"12",location))
    b12.place(x=990,y=300)

    b13=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b13,"13",location))
    b13.place(x=1070,y=300)

    b14=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b14,"14",location))
    b14.place(x=1150,y=300)

    b15=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b15,"15",location))
    b15.place(x=1230,y=300)

    b16=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b16,"16",location))
    b16.place(x=1310,y=300)

    b17=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b17,"17",location))
    b17.place(x=1390,y=300)

    b18=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b18,"18",location))
    b18.place(x=1470,y=300)

    b19=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b19,"19",location))
    b19.place(x=830,y=350)

    b20=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b20,"20",location))
    b20.place(x=910,y=350)

    b21=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b21,"21",location))
    b21.place(x=990,y=350)

    b22=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b22,"22",location))
    b22.place(x=1070,y=350)

    b23=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b23,"23",location))
    b23.place(x=1150,y=350)

    b24=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b24,"24",location))
    b24.place(x=1230,y=350)

    b25=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b25,"25",location))
    b25.place(x=1310,y=350)

    b26=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b26,"26",location))
    b26.place(x=1390,y=350)

    b27=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b27,"27",location))
    b27.place(x=1470,y=350)

    b28=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b28,"28",location))
    b28.place(x=830,y=400)

    b29=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b29,"29",location))
    b29.place(x=910,y=400)

    b30=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b30,"30",location))
    b30.place(x=990,y=400)

    b31=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b31,"31",location))
    b31.place(x=1070,y=400)

    b32=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b32,"32",location))
    b32.place(x=1150,y=400)

    b33=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b33,"33",location))
    b33.place(x=1230,y=400)

    b34=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b34,"34",location))
    b34.place(x=1310,y=400)

    b35=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b35,"35",location))
    b35.place(x=1390,y=400)

    b36=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b36,"36",location))
    b36.place(x=1470,y=400)

    b37=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b37,"37",location))
    b37.place(x=830,y=450)

    b38=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b38,"38",location))
    b38.place(x=910,y=450)

    b39=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b39,"39",location))
    b39.place(x=990,y=450)

    b40=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b40,"40",location))
    b40.place(x=1070,y=450)

    b41=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b41,"41",location))
    b41.place(x=1150,y=450)

    b42=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b42,"42",location))
    b42.place(x=1230,y=450)

    b43=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b43,"43",location))
    b43.place(x=1310,y=450)

    b44=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b44,"44",location))
    b44.place(x=1390,y=450)

    b45=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b45,"45",location))
    b45.place(x=1470,y=450)

    b46=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b46,"46",location))
    b46.place(x=830,y=500)

    b47=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b47,"47",location))
    b47.place(x=910,y=500)

    b48=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b48,"48",location))
    b48.place(x=990,y=500)

    b49=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b49,"49",location))
    b49.place(x=1070,y=500)

    b50=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b50,"50",location))
    b50.place(x=1150,y=500)

    b51=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b51,"51",location))
    b51.place(x=1230,y=500)

    b52=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b52,"52",location))
    b52.place(x=1310,y=500)

    b53=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b53,"53",location))
    b53.place(x=1390,y=500)

    b54=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b54,"54",location))
    b54.place(x=1470,y=500)

    b55=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b55,"55",location))
    b55.place(x=830,y=550)

    b56=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b56,"56",location))
    b56.place(x=910,y=550)

    b57=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b57,"57",location))
    b57.place(x=990,y=550)

    b58=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b58,"58",location))
    b58.place(x=1070,y=550)

    b59=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b59,"59",location))
    b59.place(x=1150,y=550)

    b60=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b60,"60",location))
    b60.place(x=1230,y=550)

    b61=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b61,"61",location))
    b61.place(x=1310,y=550)

    b62=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b62,"62",location))
    b62.place(x=1390,y=550)

    b63=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b63,"63",location))
    b63.place(x=1470,y=550)

    b64=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b64,"64",location))
    b64.place(x=830,y=600)

    b65=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b65,"65",location))
    b65.place(x=910,y=600)

    b66=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b66,"66",location))
    b66.place(x=990,y=600)

    b67=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b67,"67",location))
    b67.place(x=1070,y=600)

    b68=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b68,"68",location))
    b68.place(x=1150,y=600)

    b69=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b69,"69",location))
    b69.place(x=1230,y=600)

    b70=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b70,"70",location))
    b70.place(x=1310,y=600)

    b71=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b71,"71",location))
    b71.place(x=1390,y=600)

    b72=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b72,"72",location))
    b72.place(x=1470,y=600)

    b73=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b73,"73",location))
    b73.place(x=830,y=650)

    b74=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b74,"74",location))
    b74.place(x=910,y=650)

    b75=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b75,"75",location))
    b75.place(x=990,y=650)

    b76=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b76,"76",location))
    b76.place(x=1070,y=650)

    b77=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b77,"77",location))
    b77.place(x=1150,y=650)

    b78=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b78,"78",location))
    b78.place(x=1230,y=650)

    b79=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b79,"79",location))
    b79.place(x=1310,y=650)

    b80=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b80,"80",location))
    b80.place(x=1390,y=650)

    b81=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b81,"81",location))
    b81.place(x=1470,y=650)

    b82=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b82,"82",location))
    b82.place(x=830,y=700)

    b83=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b83,"83",location))
    b83.place(x=910,y=700)

    b84=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b84,"84",location))
    b84.place(x=990,y=700)

    b85=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b85,"85",location))
    b85.place(x=1070,y=700)
    b86=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b86,"86",location))
    b86.place(x=1150,y=700)

    b87=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b87,"87",location))
    b87.place(x=1230,y=700)

    b88=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b88,"88",location))
    b88.place(x=1310,y=700)

    b89=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b89,"89",location))
    b89.place(x=1390,y=700)

    b90=Button(root,height=1,width=5,cursor="hand2",command=lambda:check_slot(b90,"90",location))
    b90.place(x=1470,y=700)

    #Mapping the buttons according to status
    button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
                b11,b12,b13,b14,b15,b16,b17,b18,b19,b20
                ,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,
                b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,
                b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,
                b83,b84,b85,b86,b87,b88,b89,b90]
    
    i=1
    for ele in button_list:
        button_status(ele,str(i),location)
        i+=1
        