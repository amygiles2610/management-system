from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import subprocess


class main:
    def __init__(self,master):
        self.master = master
        
        frame = Frame(master, width=200, height=250)
        frame.place(x=10,y=20)
        frame.config(padx=30,pady=5)
        frame.config(bg='white')

        self.hour='12'

        self.hour_label=Label(frame,text=self.hour,bg='white',font='ansi 16')
        self.hour_label.grid(row=2,column=1,padx=20)
        
        def increase_hour_control():
            self.hour=self.hour_label.cget("text")
            if self.hour=='12':
                self.hour='01'
                self.hour_label.config(text=self.hour)
            else:
                self.hour = int(self.hour)
                self.hour=self.hour+1
                if len(str(self.hour))<2:
                    self.hour='0'+str(self.hour)
                    self.hour_label.config(text=self.hour)
                else:
                    self.hour_label.config(text=str(self.hour))

        self.increase_hour_icon = PhotoImage(file="UpwardArrow.png")
        self.increase_hour_button = Button(frame,width=20, height=20,image=self.increase_hour_icon,command=increase_hour_control,bg='white',borderwidth=0)
        self.increase_hour_button.grid(row=1,column=1,pady=10)

        def decrease_hour_control():
            self.hour=self.hour_label.cget("text")
            if self.hour=='01':
                self.hour='12'
                self.hour_label.config(text=self.hour)
            else:
                self.hour = int(self.hour)
                self.hour=self.hour-1
                if len(str(self.hour))<2:
                    self.hour='0'+str(self.hour)
                    self.hour_label.config(text=self.hour)
                else:
                    self.hour_label.config(text=str(self.hour))

        self.decrease_hour_icon = PhotoImage(file="DownwardArrow.png")
        self.decrease_hour_button = Button(frame,width=20, height=20,image=self.decrease_hour_icon,command=decrease_hour_control,bg='white',borderwidth=0)
        self.decrease_hour_button.grid(row=3,column=1,pady=10)

        self.colon_label=Label(frame,text=':',font='ansi 16',bg='white',width=0)
        self.colon_label.grid(row=2,column=2)
        
        self.minuet='00'

        self.minuet_label=Label(frame,text=self.minuet,bg='white',font='ansi 16')
        self.minuet_label.grid(row=2,column=3,padx=20)
        
        def increase_minuet_control():
            self.minuet=self.minuet_label.cget("text")
            if self.minuet=='59':
                self.minuet='00'
                self.minuet_label.config(text=self.minuet)
            else:
                self.minuet = int(self.minuet)
                self.minuet=self.minuet+1
                if len(str(self.minuet))<2:
                    self.minuet='0'+str(self.minuet)
                    self.minuet_label.config(text=self.minuet)
                else:
                    self.minuet_label.config(text=str(self.minuet))

        
        self.increase_minuet_icon = PhotoImage(file="UpwardArrow.png")
        self.increase_minuet_button = Button(frame,width=20, height=20,image=self.increase_minuet_icon,command=increase_minuet_control,bg='white',borderwidth=0)
        self.increase_minuet_button.grid(row=1,column=3)

        def decrease_minuet_control():
            self.minuet=self.minuet_label.cget("text")
            if self.minuet=='00':
                self.minuet='59'
                self.minuet_label.config(text=self.minuet)
            else:
                self.minuet = int(self.minuet)
                self.minuet=self.minuet-1
                if len(str(self.minuet))<2:
                    self.minuet='0'+str(self.minuet)
                    self.minuet_label.config(text=self.minuet)
                else:
                    self.minuet_label.config(text=self.minuet)
                    
        self.decrease_minuet_icon = PhotoImage(file="DownwardArrow.png")
        self.decrease_minuet_button = Button(frame,width=20, height=20,image=self.decrease_minuet_icon,command=decrease_minuet_control,bg='white',borderwidth=0)
        self.decrease_minuet_button.grid(row=3,column=3)


        self.day_state='AM'

        self.day_state_label=Label(frame,text=self.day_state,bg='white',font='ansi 16')
        self.day_state_label.grid(row=2,column=4,padx=20)

        def up_state_control():
            self.day_state=self.day_state_label.cget("text")
            if self.day_state == 'AM':
                self.day_state='PM'
                self.day_state_label.config(text=self.day_state)
            else:
                self.day_state == 'PM'
                self.day_state='AM'
                self.day_state_label.config(text=self.day_state)

        self.up_state_icon = PhotoImage(file="UpwardArrow.png")
        self.up_state_button = Button(frame,width=20, height=20,image=self.up_state_icon,command=up_state_control,bg='white',borderwidth=0)
        self.up_state_button.grid(row=1,column=4)
        
        def down_state_control():
            self.day_state=self.day_state_label.cget("text")
            if self.day_state == 'AM':
                self.day_state='PM'
                self.day_state_label.config(text=self.day_state)
            else:
                self.day_state == 'PM'
                self.day_state='AM'
                self.day_state_label.config(text=self.day_state)

        self.down_state_icon = PhotoImage(file="DownwardArrow.png")
        self.down_state_button = Button(frame,width=20, height=20,image=self.down_state_icon,command=down_state_control,bg='white',borderwidth=0)
        self.down_state_button.grid(row=3,column=4)

        empty_label=Label(frame,text='',bg='white')
        empty_label.grid(row=5,column=4)

        def set_time():
            picked_time= str(self.hour_label)+'-'+str(self.minuet_label)+' '+str(self.day_state_label)
            file=open("SetTime.txt","w")
            file.write(picked_time)
            file.close()
            master.destory()
            
        self.set_button = Button(frame,width=6,height=1,text='Set',bg='#db124b',fg='white',font='ansi 10 underline',command=set_time)
        self.set_button.grid(row=6,column=4)

        self.cancel_button = Button(frame,width=6,height=1,text='Cancel',bg='#F04979',fg='white',font='ansi 10',command=master.destroy)
        self.cancel_button.grid(row=6,column=3)


            

root = Tk()
root.title("Time Picker")
root.geometry("300x200")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
                
