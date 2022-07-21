# Code by @AmirMotefaker

# Alarm Clock

# Importing required modules
from tkinter import *
import datetime
import time
import winsound
   """ Tkinter module: Helps us to create a window for the user to use the application
       datetime and time modules: Help us to handle dates and time and manipulate them when needed.
       winsound module: Helpful to generate sounds for our alarm clock. """
 
def Alarm(set_alarm_timer):
    """ Creating a function for the alarm """
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            break
 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
 
   """ Creating the Tkinter Window """
window = Tk()
window.title("Alarm Clock -Amir Motefaker-")
window.geometry("400x160")
window.config(bg="#76b5c5")
window.resizable(width=False,height=False)
 
time_format=Label(window, text= "Remember to set time in 24 hour format!", fg="white",bg="#922B21",font=("Arial",15)).place(x=20,y=120)
addTime = Label(window,text = "Hour       Min         Sec",font=60,fg="white",bg="black").place(x = 212, y=3)
setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="white",bg="#873e23",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=35)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
 
hourTime= Entry(window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=210,y=40)
minTime= Entry(window,textvariable = min,bg = "#48C9B0",width = 4,font=(20)).place(x=270,y=40)
secTime = Entry(window,textvariable = sec,bg = "#48C9B0",width = 4,font=(20)).place(x=330,y=40)
 
submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#D4AC0D",width = 15,command = get_alarm_time,font=(20)).place(x =130,y=80)
 
window.mainloop()
