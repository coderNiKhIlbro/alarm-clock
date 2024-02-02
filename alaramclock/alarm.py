import tkinter as tk
from tkinter import *
import datetime
import pygame
from threading import *
import time
import os
from tkinter import messagebox

class AlarmClock:
    id =0
    posx =0
    posy=-100
    snoozed =0
    set_alarm_time = "00:00:00"
    def __init__(self, root):
        self.incr_process()
        self.hour = StringVar(value="00")
        self.minute = StringVar(value="00")
        self.second = StringVar(value="00")
        self.ampm = StringVar(value="AM")
        self.select = StringVar(value="alarm.mp3")
        self.snooze = StringVar(value="5 mins")
        self.label = StringVar(value="Good Morning")

        self.ringTone = os.listdir("E:/Python projects/ALARAMCLOCK/RingTones")
        self.ONImg = "Images/ON.png"
        self.OFFImg = "Images/off.png"

        self.Started = False
        self.ON_Btn = None
        self.OFF_Btn = None
        self.ON_Btn = PhotoImage(file=self.ONImg)
        self.OFF_Btn = PhotoImage(file=self.OFFImg)
        self.ringicon=PhotoImage(file="Images/ringtone.png")
        self.editicon = PhotoImage(file="Images/edit.png")
        self.savebtn = PhotoImage(file="Images/save.png")
        self.canclebtn = PhotoImage(file="Images/cancle.png")



        self.add_alarm()
        # alarmEnd(self)

    # def create_widgets(self):
    #     pass

    def add_alarm(self):
        
        print()
        frame1 = Frame(canvas, bg="white")
        canvas.create_window((self.posx, self.posy), window=frame1, anchor="n")
        frame1.pack( fill=X, padx=10,pady=10)
       
         # Create a window to hold the frame

        self.lable1 = Label(frame1, text="00:00", font=("Helvetica 30 bold"),bg='white')
        self.lable1.pack(anchor=NW, padx=(10,0), pady=10, side=LEFT)

        self.label2 = Label(frame1,text="am",font=("Helvetica 10 bold"), bg='white')
        self.label2.pack(side=BOTTOM,anchor=W)
        frame1.bind("<Button-1>", self.label_clicked)
        self.lable1.bind("<Button-1>", self.label_clicked)
        self.btn = Button(frame1, text="btn", command=self.Threading, image=self.OFF_Btn, relief=FLAT,bg="white")
        self.btn.pack(anchor=NW, side=RIGHT, padx=(0, 10), pady=(5, 0))
    
        print(self.posx, self.posy)


    def label_clicked(self, event):
        self.set_Time_frame()

    def set_Time_frame(self):
        root.withdraw()
        self.time_frm =time_frm= Toplevel(bg="white")
        time_frm.geometry(root.winfo_geometry())
        Label(time_frm, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red",bg="white").pack(pady=10)
        Label(time_frm, text="Set Time", font=("Helvetica 15 bold"),bg="white").pack()
        frame = Frame(time_frm,bg="white")
        frame.pack()
        hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                 '08', '09', '10', '11', '12')
        # self.hour.set(hours)
        hrs = OptionMenu(frame, self.hour, *hours)
        hrs.config(bg="white")
        hrs.pack(side=LEFT)

        minutes = tuple("{:02d}".format(i) for i in range(60))
        # self.minute.set(minutes[0])
        mins = OptionMenu(frame, self.minute, *minutes)
        mins.pack(side=LEFT)
        mins.config(bg="white")


        seconds = tuple("{:02d}".format(i) for i in range(60))
        # self.second.set(seconds[0])
        secs = OptionMenu(frame, self.second, *seconds)
        secs.pack(side=LEFT)
        secs.config(bg="white")


        ampmVal = ('AM','PM')
        ampm = OptionMenu(frame,self.ampm,*ampmVal)
        ampm.pack(side=LEFT)
        ampm.config(bg="white")


        frame3 = Frame(time_frm,bg="white")
        frame3.pack(pady=20)

        EntryLbl = Label(frame3, text="Label", font=("Helvetica 12 bold"),image=self.editicon,bg='white')
        EntryLbl.grid(column=0,row=0)
        self.Display_msg = Entry(frame3,font=("Helvetica 12 bold"),width=20)
        # self.Display_msg.pack(padx=(20, 0), pady=20, fill=X, side=LEFT)
        self.Display_msg.grid(column=1,row=0,padx=10,sticky=W)

        self.Display_msg.insert(0, self.label.get())
        self.Display_msg.bind("<KeyRelease>", self.on_label_change)
        # frame4 = Frame(time_frm)
        # frame4.pack(pady=20)
        list_lbl = Label(frame3, text="RingTone", font=("Helvetica 12 bold"),image=self.ringicon,bg='white')
        # list_lbl.pack(side=LEFT)
        list_lbl.grid(column=0,row=1,pady=20)
       
        # self.select.set(self.ringTone[0])
        Option_Menu = OptionMenu(frame3, self.select, *self.ringTone)
        Option_Menu.config(width=20,font=("Helvetica 10 "),bg='white')
        # Option_Menu.pack(padx=(20, 0), pady=20, fill=X, side=LEFT)
        Option_Menu.grid(column=1,row=1,padx=10,sticky=W)

        snoozelbl =Label(frame3, text="sne", font=("Helvetica 12 bold"),bg='white')
        snoozelbl.grid(column=0,row=2,pady=20)

        snooze = ("5 mins","10 mins","15 mins","20 mins","30 mins")
        snoozeOption = OptionMenu(frame3,self.snooze,*snooze)
        snoozeOption.config(width=20,font=("Helvetica 10 "),bg='white')
        snoozeOption.grid(column=1,row=2,padx=10,sticky=W)

        Button(time_frm, text="Save", font=("Helvetica 20 bold"), command=self.on_Save,image=self.savebtn,relief=FLAT,bg='white').pack(anchor=S, side=LEFT,
                                                                                             padx=(20, 0),
                                                                                             pady=(0, 20))
        Button(time_frm, text="Cancel", font=("Helvetica 20 bold"), command=self.on_cancel,image=self.canclebtn,relief=FLAT,bg='white').pack(anchor=S, side=RIGHT,
                                                                                                  padx=(0, 20),
                                                                                                  pady=(0, 20))

    def on_label_change(self, event):
        self.label.set(self.Display_msg.get())
        print(self.label.get())

    def on_Save(self):
        self.time_frm.destroy()
        self.lable1.config(text=f"{self.hour.get()}:{self.minute.get()}")
        self.set_alarm_time = f"{self.hour.get()}:{self.minute.get()}:{self.second.get()}"
        root.deiconify()

    def on_cancel(self):
        self.time_frm.destroy()
        root.deiconify()

    def Threading(self):
        if not self.Started:
            t1 = Thread(target=self.alarm)
            t1.start()
            self.Started = True
            self.btn.configure(image=self.ON_Btn)
        elif self.Started:
            self.Started = False
            self.btn.configure(image=self.OFF_Btn)

    def alarm(self):
        while True:
            time.sleep(1)
            if self.snoozed == 0:
                self.set_alarm_time = f"{self.hour.get()}:{self.minute.get()}:{self.second.get()}:{self.ampm.get()}"
            
            current_time = datetime.datetime.now().strftime("%I:%M:%S:%p")
            print(current_time, self.set_alarm_time)
            if current_time == self.set_alarm_time:
                print("Time to Wake up")
                play_sound(f"RingTones\{self.select.get()}")
                self.alarmEnd()
                break
            if not self.Started:
                break

    def incr_process(self):
        AlarmClock.id+=1
        AlarmClock.posy+=100




    def alarmEnd(self):
        self.notify_widget=Toplevel()
        screenh=root.winfo_screenheight()
        screenw=root.winfo_screenwidth()
        geostr = f"280x200+{screenw-300}+{screenh-300}"
        self.notify_widget.geometry(geostr)
        self.notify_widget.title("Alarm")

        # lbl=Label(notify_widget,text=self.label.get(),font=("Helvetica 15 bold"))
        # lbl.pack(side=TOP)

        # Label(notify_widget,text="Label").pack(side=TOP)
        # Label(notify_widget,text=self.set_alarm_time,font=("Helvetica 15 bold"))


        # snooze_Button=Button(notify_widget,text='snooze',bg='white')
        # snooze_Button.pack(side=LEFT,anchor=SW)

        # calcle_btn=Button(notify_widget,text='cancle',bg='white')
        # snooze_Button.pack(side=LEFT,anchor=SE)
        lbl=Label(self.notify_widget,text="Morning",font=("Helvetica 15 bold"))
        lbl.pack(side=TOP,anchor=W,padx=20)

        Label(self.notify_widget,text='00:00',font=("Helvetica 15 bold")).pack(side=TOP,anchor=W,padx=20,pady=(10,0))

        snooze_Button=Button(self.notify_widget,text='snooze',bg='white',font=("Helvetica 15 bold"),command=lambda:snooze(self))
        snooze_Button.pack(side=LEFT,anchor=SW,padx=20,pady=20)

        calcle_btn=Button(self.notify_widget,text='cancle',bg='white',font=("Helvetica 15 bold"))
        calcle_btn.pack(side=RIGHT,anchor=SE,padx=20,pady=20)
        time.sleep(10)
        self.notify_widget.destroy()
        pygame.quit()


################classs is over##############################

def snooze(self):
    self.notify_widget.destroy()
    pygame.quit()
    snoozedTime = int(self.minute.get())+int(self.snooze.get().split()[0])
    print("snooed time",snoozedTime)
    if snoozedTime <10:
        snoozedTime = f'0{snoozedTime}'
    
    self.set_alarm_time = f"{self.hour.get()}:{snoozedTime}:{self.second.get()}:{self.ampm.get()}"
    print(self.set_alarm_time)
    self.snoozed += 1
    self.alarm()
    




def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()





def window_changed(event):
    root.update_idletasks()

    w=root.winfo_width()
    h =root.winfo_height()
    
    addbtn.place(x=w-60,y=h-60)



def on_close():
    print("closed")
    root.withdraw()

def mainMethod():
    if AlarmClock.id<5:
        obj=AlarmClock(root)
        process[obj.id]=obj
    else:
        messagebox.showerror("Limit exceed","Limeddd")
    print(process)
    pass


if __name__ == "__main__":

    process={}
    root = tk.Tk()
    
    root.geometry("300x500+600+100")
    root.title("Alarm")
    # alarm_clock = AlarmClock(root)
    root.bind("<Configure>",window_changed)

# Create a Canvas widget

    canvas = Canvas(root,bg='#EDEDED')
    canvas.pack(side="left" ,fill="both",expand=True)
        


    frame2 = Frame(root, bg="white")
    frame2.pack(side="bottom", anchor="se")
    addimg = PhotoImage(file="Images/btn.png", master=frame2)
    addbtn = Button(root, image=addimg, command=mainMethod, relief=FLAT,background="#EDEDED")
    addbtn.pack(padx=10, pady=10)
    frmImg = PhotoImage(file="Images/bg.png")

    w=root.winfo_width()
    h =root.winfo_height()
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    # addbtn.place(x=w-80,y=h-80)
    # print(root.winfo_screenwidth())
    # alarmEnd()
    root.mainloop()