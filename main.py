from tkinter import *
from PIL import Image,ImageTk
import subprocess
import sys

def manager_interface():#Function to open manager interface
    root.destroy()
    subprocess.Popen([sys.executable, 'manager_interface.py'])
 
def customer_interface():#Function to open customer interface
    root.quit()
    import customer_interface 


global root
root=Tk()

def main():
   
    root.geometry('1920x880')

    logo_lbl=Label(text="Car Parking",font=("courier",40,"bold")).pack()#Label for logo

    manager_button=Button(text="Manager",font=("courier",30,"bold"),width=10,height=2,bg="black",fg="white",
                            command=manager_interface)#Button to call manager_interface function
    manager_button.place(x=300,y=350)

    user_button=Button(text="Customer",font=("courier",30,"bold"),width=10,height=2,bg="black",fg="white",
                        command=customer_interface)#Button to call customer_interface function
    user_button.place(x=950,y=350)

    root.mainloop()
main()