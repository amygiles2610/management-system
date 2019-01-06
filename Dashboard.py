from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import subprocess


class main:
    def __init__(self,master):
        self.master = master
        
        frame = Frame(master)
        frame.place(x=10,y=20)
        frame.config(padx=30,pady=5)
        frame.config(bg='white')
        
        def calendar_page():
            subprocess.call("CalendarFrontPage.py", shell=True)

        self.calendar_icon = PhotoImage(file="CalendarIconBig.png")
        self.calendar_button = Button(frame,width=50, height=50,command=calendar_page,bg='white',borderwidth=0)
        self.calendar_button.grid(row=1,column=1,pady=10)

        self.calendar_button.config(image=self.calendar_icon)
        self.calendar_button.image = self.calendar_icon

        self.calendar_label=Label(frame,text='Calendar',bg='white',font='ansi 16')
        self.calendar_label.grid(row=2,column=1,padx=20)

        def time_tracking_page():
            subprocess.call("TimeTracking.py", shell=True)

        self.clock_icon = PhotoImage(file="ClockIconBig.png")
        self.clock_button = Button(frame,width=50, height=50,bg='white',borderwidth=0,command=time_tracking_page)
        self.clock_button.grid(row=1,column=2,pady=10)

        self.clock_button.config(image=self.clock_icon)
        self.clock_button.image = self.clock_icon

        self.clock_label=Label(frame,text='Time Tracking',font='ansi 16',bg='white',width=0)
        self.clock_label.grid(row=2,column=2)

        self.projects_icon = PhotoImage(file="FolderIconBig.png")
        self.projects_button = Button(frame,width=50, height=50,bg='white',borderwidth=0)
        self.projects_button.grid(row=1,column=3)

        self.projects_button.config(image=self.projects_icon)
        self.projects_button.image = self.projects_icon

        self.projects_label=Label(frame,text='Projects',bg='white',font='ansi 16')
        self.projects_label.grid(row=2,column=3,padx=20)

        self.checklist_icon = PhotoImage(file="ChecklistIconBig.png")
        self.checklist_button = Button(frame,width=50, height=50,image=self.checklist_icon,bg='white',borderwidth=0)
        self.checklist_button.grid(row=1,column=4)

        self.checklist_button.config(image=self.checklist_icon)
        self.checklist_button.image = self.checklist_icon

        self.checklist_label=Label(frame,text='Checklists',bg='white',font='ansi 16')
        self.checklist_label.grid(row=2,column=4,padx=20)

        self.clientForms_icon = PhotoImage(file="ClientFormsIconBig.png")
        self.clientForms_button = Button(frame,width=50, height=50,image=self.clientForms_icon,bg='white',borderwidth=0)
        self.clientForms_button.grid(row=1,column=5)

        self.clientForms_button.config(image=self.clientForms_icon)
        self.clientForms_button.image = self.clientForms_icon

        self.clientForms_label=Label(frame,text='Client Forms',bg='white',font='ansi 16')
        self.clientForms_label.grid(row=2,column=5,padx=20)
            

root = Tk()
root.title("Dashboard")
root.geometry("1000x600")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
                

