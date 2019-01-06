from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import subprocess


class main:
    def __init__(self,master):
        self.master = master

        self.frames={}

        for F in (client_details, delivery_dates):
            frame=F(master,self)
            self.frames[F]=frame
            #frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(client_details)
        
        def show_frame(self, cont):
            frame=self.frames[cont]
            frame.tkraise()
            

class client_details():
        def __init__(self,master,controller):
            self.master=master
            
            frame = Frame(master)
            frame.place(x=10,y=20)
            frame.config(padx=30,pady=5)
            frame.config(bg='white')

            self.sub_section_label=Label(frame,text='Company details',font='ansi 12 bold')
            self.sub_section_label.grid(row=1,column=1)

            self.entry1_label=Label(frame,text='Client name:',font='ansi 10',bg='white')
            self.entry1_label.grid(row=2,column=1)

            self.entry1=Entry(frame)
            self.entry1.grid(row=2,column=2)

            self.entry2_label=Label(frame,text='Record label:',font='ansi 10',bg='white')
            self.entry2_label.grid(row=3,column=1)

            self.entry2=Entry(frame)
            self.entry2.grid(row=3,column=2)

            self.entry3_label=Label(frame,text='Music group:',font='ansi 10',bg='white')
            self.entry3_label.grid(row=4,column=1)
        
            self.entry3=Entry(frame)
            self.entry3.grid(row=4,column=2)

            self.button=Button(frame,text='Next page',command=lambda:controller.show_frame(delivery_dates))
            self.button.grid(row=5,column=1)

class delivery_dates():
    def __init__(self,master,controller):
            self.master=master
            
            frame = Frame(master)
            frame.place(x=10,y=20)
            frame.config(padx=30,pady=5)
            frame.config(bg='pink')
            
            self.sub_section_label=Label(frame,text='Comgdfgdfgs',font='ansi 12 bold')
            self.sub_section_label.grid(row=1,column=1)

            self.entry1_label=Label(frame,text='Cliefhdhme:',font='ansi 10',bg='white')
            self.entry1_label.grid(row=2,column=1)

            self.entry1=Entry(frame)
            self.entry1.grid(row=2,column=2)

            self.entry2_label=Label(frame,text='Recfdhabel:',font='ansi 10',bg='white')
            self.entry2_label.grid(row=3,column=1)

            self.entry2=Entry(frame)
            self.entry2.grid(row=3,column=2)

            self.entry3_label=Label(frame,text='Music group:',font='ansi 10',bg='white')
            self.entry3_label.grid(row=4,column=1)
        
            self.entry3=Entry(frame)
            self.entry3.grid(row=4,column=2)

            self.button1=Button(frame,text='Back page',command=lambda:controller.show_frame(client_details))
            self.button1.grid(row=5,column=1)
            
root = Tk()
root.title("Time Picker")
root.geometry("1000x600")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
