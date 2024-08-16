from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime,sys,subprocess
import database
import profile_
def frontpage(details):
    infos = database.give_info_for_location()
    # location = infos[0][0][0]
    # available = infos[0][0][2]
    # booked = infos[0][0][1]
    # totalspaces = available+booked
    user_name = details[0][0]


    def createFrame(frame):
        locname = Label(frame, text=f"{location}", fg='white',height=1,bg='black',width=10,font=('Trebuchet MS', 20))
        locname.place(x=5,y=15)
        Label(frame, text=f"Total spaces:",font=('Trebuchet MS', 10), fg='white',height=1,bg='black').place(x=345,y=6)
        total = Label(frame, text=f"{totalspaces}",font=('Trebuchet MS', 10), fg='white',height=1,bg='black')
        total.place(x=420,y=6)
        Label(frame, text=f"Available spaces:",font=('Trebuchet MS', 10), fg='white',height=1,bg='black').place(x=325,y=26)
        availables = Label(frame, text=f"{available}",font=('Trebuchet MS', 10), fg='white',height=1,bg='black')
        availables.place(x=420,y=26)
        Label(frame, text="Parking rate: Rs25/hr",font=('Trebuchet MS', 10), fg='white',height=1,bg='black').place(x=325,y=46)

    
            # self.locname = Label(frame, text="parkingrate:", bg='black')
            # self.locname.place(x=10,y=10)


    frames = []
    root=Tk()
    root.geometry("1545x880")
    root.resizable(False,False)
    root_image = Image.open("resources/clear_bg.jpeg")
    root_photo = ImageTk.PhotoImage(root_image.resize((1920, 880)))

    canvas = Canvas(root, width=1920, height=880)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=root_photo, anchor="nw")

    logo_image=Image.open("resources/logo.png")
    logo_photo=ImageTk.PhotoImage(logo_image.resize((70,70)))
    canvas.create_image(35, 35, image=logo_photo, anchor="nw")

    name=canvas.create_text(140, 40, text="Easy Parking", font=('Trebuchet MS', 40, "bold"), fill='#70B6AC')
    canvas.coords(name, 270, 65)
    def prof():
        profile_.profile_infos(details,root)


    loc = Frame(root,bg="#70B6AC",height=535,width=570,borderwidth=10,relief=RAISED)
    loc.place(x=70,y=188)
    yaxis = 100


    profile_image=Image.open("resources/profile_logo.png")
    profile_photo=ImageTk.PhotoImage(profile_image.resize((100,100)))
    btn = Button(root,image=profile_photo,height=73,borderwidth=0,width=73,command=prof)
    btn.place(x=1400,y=20)

    Frame(root, width=1920, height=2, bg='white').place(x=0, y=120)

    res = Frame(root,bg='white',height=399,width=374)
    res.place(x=1014,y=257)



    yaxis=60
    for location_info in infos:
        # print(location_info)
        location = location_info[0][3]
        booked = location_info[0][1]
        available = location_info[0][2]
        totalspaces = booked + available
        # continue

        frame = Frame(loc,bg='black',height=80,width=500,borderwidth=5,relief=RAISED)
        frame.place(x=30,y=yaxis)
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
            frame.place_configure(x=30, y=new_y)  # Update the frame's position
        # print(frames)
    scale_float = DoubleVar(value=1)
    scale=Scale(root,command =update_positions,
                    bg='white',
                    fg='white',
                    from_ = 0,
                    to = len(infos) * 30,
                    length = 525,
                    orient = VERTICAL,
                    variable=scale_float,
                    borderwidth=0
                    )

    scale.place(x=640,y=190)

    root.mainloop()
# frontpage('a')
