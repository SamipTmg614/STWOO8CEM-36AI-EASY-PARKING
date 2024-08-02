from tkinter import *
import datetime
import database
root=Tk()
root.geometry("1920x880")



def green(button,x):
    conn=database.makeconnection()
    c=conn.cursor()
    button.config(text="available",bg="green")
    c.execute(f'''UPDATE availability
                    SET status=?,model=NULL,number=NULL
                    WHERE id=? 
                  ''',("TRUE",x))
    conn.commit()
    conn.close()
    
#Function to change the button colour and text
def red(button,x):
    conn=database.makeconnection()
    c=conn.cursor()
    button.config(text="booked",bg="red")
    model=model_var.get()
    number=number_var.get()

    c.execute(f'''UPDATE availability
                    SET status=?,model=?,number=?
                    WHERE id=? 
                ''',("FALSE",model,number,x))
        
    conn.commit()
    conn.close()
   
def check_availability(button,x):
    conn=database.makeconnection()
    c=conn.cursor()

    #Code to change the colour and text of the button according to the status
    c.execute("SELECT status from availability WHERE id=?",(x,))
    status=c.fetchone()
    if status[0]=="FALSE":
        win=Toplevel()
        win.geometry("300x300")
        c.execute("SELECT model,number FROM availability WHERE id=?",x)
        details=c.fetchmany()

        detail_label=Label(win,text="Details")
        detail_label.place(x=65,y=0)
        model_label=Label(win,text=f"Model:{details[0][0]}")
        model_label.place(x=0,y=20)
        number_label=Label(win,text=f"Number:{details[0][1]}")
        number_label.place(x=0,y=40)
        time_label=Label(win,text="Entry Time:")
        time_label.place(x=0,y=60)

        confirm=Button(win,text="Confirm",command=lambda:[green(button,x),win.destroy()])
        confirm.place(x=65,y=80)
        win.mainloop()
    else:
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
        time=str(t.hour)+":"+str(t.minute)
        time_label=Label(win,text=f"Time:  {time}")
        time_label.place(x=10,y=50)

        submit=Button(win,text="Submit",command=lambda:[red(button,x),win.destroy()])
        submit.place(x=80,y=80)

        win.mainloop()

    conn.commit()
    conn.close()

def button_status(button,x):
    conn=database.makeconnection()
    c=conn.cursor()
    c.execute("SELECT status from availability WHERE id=?",(x,))
    status=c.fetchone()
    if status[0]=="TRUE":
        button.config(text="available",bg="green")  
    else:
        button.config(text="booked",bg="red") 
    conn.close() 

database.availability_table()

#Frame for logo
logo=Frame(root,bg="blue",width=30,height=150,borderwidth=15)
logo.pack(fill=X)
lbl1=Label(logo,text="test")
lbl1.pack()

#Frame for available spaces
spaces=Frame(root,width=700,height=880,borderwidth=4,relief=GROOVE)
spaces.pack(side=RIGHT)
lbl2=Label(spaces,text="Available Spaces",font=("courier",19,"bold"))
lbl2.place(x=270)

#32 Buttons for 32 spaces
b1=Button(spaces,height=2,width=15,command=lambda:check_availability(b1,"1"))
b1.place(x=20,y=120)

b2=Button(spaces,height=2,width=15,command=lambda:check_availability(b2,"2"))
b2.place(x=190,y=120)

b3=Button(spaces,height=2,width=15,command=lambda:check_availability(b3,"3"))
b3.place(x=370,y=120)

b4=Button(spaces,height=2,width=15,command=lambda:check_availability(b4,"4"))
b4.place(x=550,y=120)

b5=Button(spaces,height=2,width=15,command=lambda:check_availability(b5,"5"))
b5.place(x=20,y=200)

b6=Button(spaces,height=2,width=15,command=lambda:check_availability(b6,"6"))
b6.place(x=190,y=200)

b7=Button(spaces,height=2,width=15,command=lambda:check_availability(b7,"7"))
b7.place(x=370,y=200)

b8=Button(spaces,height=2,width=15,command=lambda:check_availability(b8,"8"))
b8.place(x=550,y=200)

b9=Button(spaces,height=2,width=15,command=lambda:check_availability(b9,"9"))
b9.place(x=20,y=280)

b10=Button(spaces,height=2,width=15,command=lambda:check_availability(b10,"10"))
b10.place(x=190,y=280)
b11=Button(spaces,height=2,width=15,command=lambda:check_availability(b11,"11"))
b11.place(x=370,y=280)

b12=Button(spaces,height=2,width=15,command=lambda:check_availability(b12,"12"))
b12.place(x=550,y=280)

b13=Button(spaces,height=2,width=15,command=lambda:check_availability(b13,"13"))
b13.place(x=20,y=360)

b14=Button(spaces,height=2,width=15,command=lambda:check_availability(b14,"14"))
b14.place(x=190,y=360)

b15=Button(spaces,height=2,width=15,command=lambda:check_availability(b15,"15"))
b15.place(x=370,y=360)

b16=Button(spaces,height=2,width=15,command=lambda:check_availability(b16,"16"))
b16.place(x=550,y=360)

b17=Button(spaces,height=2,width=15,command=lambda:check_availability(b17,"17"))
b17.place(x=20,y=440)

b18=Button(spaces,height=2,width=15,command=lambda:check_availability(b18,"18"))
b18.place(x=190,y=440)

b19=Button(spaces,height=2,width=15,command=lambda:check_availability(b19,"19"))
b19.place(x=370,y=440)

b20=Button(spaces,height=2,width=15,command=lambda:check_availability(b20,"20"))
b20.place(x=550,y=440)

b21=Button(spaces,height=2,width=15,command=lambda:check_availability(b21,"21"))
b21.place(x=20,y=520)

b22=Button(spaces,height=2,width=15,command=lambda:check_availability(b22,"22"))
b22.place(x=190,y=520)

b23=Button(spaces,height=2,width=15,command=lambda:check_availability(b23,"23"))
b23.place(x=370,y=520)

b24=Button(spaces,height=2,width=15,command=lambda:check_availability(b24,"24"))
b24.place(x=550,y=520)

b25=Button(spaces,height=2,width=15,command=lambda:check_availability(b25,"25"))
b25.place(x=20,y=600)

b26=Button(spaces,height=2,width=15,command=lambda:check_availability(b26,"26"))
b26.place(x=190,y=600)

b27=Button(spaces,height=2,width=15,command=lambda:check_availability(b27,"27"))
b27.place(x=370,y=600)

b28=Button(spaces,height=2,width=15,command=lambda:check_availability(b28,"28"))
b28.place(x=550,y=600)

b29=Button(spaces,height=2,width=15,command=lambda:check_availability(b29,"29"))
b29.place(x=20,y=680)

b30=Button(spaces,height=2,width=15,command=lambda:check_availability(b30,"30"))
b30.place(x=190,y=680)

b31=Button(spaces,height=2,width=15,command=lambda:check_availability(b31,"31"))
b31.place(x=370,y=680)

b32=Button(spaces,height=2,width=15,command=lambda:check_availability(b32,"32"))
b32.place(x=550,y=680)

#Mapping the buttons according to status
button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
             b11,b12,b13,b14,b15,b16,b17,b18,b19,b20
             ,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32]
i=1
for ele in button_list:
    button_status(ele,str(i))
    i+=1



#Frame for locations
locations=Frame(root,width=900,height=880,relief=GROOVE,borderwidth=4)
locations.pack(side=LEFT)

btn=Button(locations,text="Location  1",height=5,width=30,background="red")
btn.place(x=30,y=120)

btn1=Button(locations,text="Location 2",height=5,width=30,background="red")
btn1.place(x=300,y=120)

btn3=Button(locations,text="Location 3",height=5,width=30,background="red")
btn3.place(x=570,y=120)

btn4=Button(locations,text="Location 4",height=5,width=30,background="red")
btn4.place(x=30,y=250)

btn5=Button(locations,text="Location 5",height=5,width=30,background="red")
btn5.place(x=300,y=250)

btn6=Button(locations,text="Location 6",height=5,width=30,background="red")
btn6.place(x=570,y=250)

btn7=Button(locations,text="Location 4",height=5,width=30,background="red")
btn7.place(x=30,y=380)

btn8=Button(locations,text="Location 8",height=5,width=30,background="red")
btn8.place(x=300,y=380)

btn9=Button(locations,text="Location 9",height=5,width=30,background="red")
btn9.place(x=570,y=380)

btn10=Button(locations,text="Location 10",height=5,width=30,background="red")
btn10.place(x=30,y=510)

btn11=Button(locations,text="Location 11",height=5,width=30,background="red")
btn11.place(x=300,y=510)

btn12=Button(locations,text="Location 12",height=5,width=30,background="red")
btn12.place(x=570,y=510)

lbl3=Label(locations,text="Locations",font=("courier",19,"bold"))
lbl3.place(x=350)

root.mainloop()
