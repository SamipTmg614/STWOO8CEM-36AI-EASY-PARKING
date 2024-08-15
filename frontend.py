from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime,sys,subprocess
import database
# import profile_
def frontpage(details):
    infos = database.give_info_for_location()
    # location = infos[0][0][0]
    # available = infos[0][0][2]
    # booked = infos[0][0][1]
    # totalspaces = available+booked
    user_name = details[0][0]


    def createFrame(frame):
        locname = Label(frame, text=f"{location}", fg='black',height=5,bg='#EACF91',width=20)
        locname.place(x=5,y=5)
        Label(frame, text=f"total spaces:", fg='black',height=1,bg='#EACF91').place(x=345,y=10)
        total = Label(frame, text=f"{totalspaces}", fg='black',height=1,bg='#EACF91')
        total.place(x=420,y=10)
        Label(frame, text=f"available spaces:", fg='black',height=1,bg='#EACF91').place(x=325,y=30)
        availables = Label(frame, text=f"{available}", fg='black',height=1,bg='#EACF91')
        availables.place(x=420,y=30)
        Label(frame, text="parking rate: Rs25/hr", fg='black',height=1,bg='#EACF91').place(x=325,y=50)

    
            # self.locname = Label(frame, text="parkingrate:", bg='black')
            # self.locname.place(x=10,y=10)


    frames = []
    root=Tk()
    root.geometry("1545x880")
    root.resizable(False,False)
    root.configure(bg='#70B6AC')

    # def prof():
    #     profile_.profile_infos(details,root)

    # img = PhotoImage(file='bg.jpg',)
    # Label(root, image=img).place(x=0,y=0)

    loc = Frame(root,bg='white',height=535,width=728)
    loc.place(x=135,y=188)
    yaxis = 100
    
    # btn = Button(root,text='profile',height=1,width=22,bg='#70B6AC',command=prof)
    # btn.place(x=1340,y=49)
    # res = Frame(root,bg='white',height=399,width=374)
    # res.place(x=1014,y=257)



    yaxis=60
    for location_info in infos:
        # print(location_info)
        location = location_info[0][3]
        booked = location_info[0][1]
        available = location_info[0][2]
        totalspaces = booked + available
        # continue

        frame = Frame(loc,bg='#EACF91',height=80,width=500)
        frame.place(x=100,y=yaxis)
        createFrame(frame)

        yaxis+=125
        try:
            totalmoney = database.calculate_time(user_name,location)
            print(totalmoney)
        except:
            print('failed')
        else:
            ...

        frames.append(frame)
    def update_positions(value,):
        y_start = 60 - int(float(value))  # Start position for frames
        for i, frame in enumerate(frames):
            new_y = y_start + i * 125  # Adjust each frame's y position based on the scale
            frame.place_configure(x=100, y=new_y)  # Update the frame's position
        # print(frames)
    scale_float = DoubleVar(value=1)
    scale=Scale(root,command =update_positions,
                    bg='black',
                    fg='#EACF91',
                    from_ = 0,
                    to = len(infos) * 30,
                    length = 500,
                    orient = VERTICAL,
                    variable=scale_float,
                    )

    scale.place(x=808,y=215)


    root.mainloop()

frontpage('a')