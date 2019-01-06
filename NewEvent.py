from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import subprocess

class main:
    def __init__(self,master):
        self.master = master
        
        frame = Frame(master, width=200, height=250)
        frame.place(x=10,y=40)
        frame.config(bg='white')

        frame2=Frame(master, width=2300,height=25)
        frame2.place(x=78,y=330)
        frame2.config(bg='white')

        def date_picker_popup():
            subprocess.call("DatePickerPopup.py", shell=True)

        def time_picker_popup():
            subprocess.call("TimePickerPopup.py", shell=True)

        self.title_label = Label(frame, text='New event', bg='white',font='ansi 12 bold')
        self.title_label.grid(row=0, column=0)

        self.event_title_label=Label(frame, text="Title:", bg='white',width=12,font='ansi 10 ')
        self.event_title_label.grid(row=2, column=0)
        self.event_title_label.config(anchor=E)

        def on_entry_click_title(event):
            if self.event_title.get() == 'Event title*':
               self.event_title.delete(0, "end")
               self.event_title.insert(0, '') 
               self.event_title.config(fg = 'black')
        def on_focusout_title(event):
            if self.event_title.get() == '':
                self.event_title.config(fg = 'grey',show='')
                self.event_title.insert(0, 'Event title*')
        
        self.event_title = Entry(frame, bd=1, width=30, font='ansi 10',borderwidth=2,highlightbackground='black')
        self.event_title.grid(row=2, column=1, pady=(10))

        self.event_title.insert(0, 'Event title*')
        self.event_title.bind('<FocusIn>', on_entry_click_title)
        self.event_title.bind('<FocusOut>', on_focusout_title)

        self.event_title.config(fg = 'grey')

        self.type_event_label=Label(frame, text="Type of event:", bg='white',width=12,font='ansi 10')
        self.type_event_label.grid(row=3, column=0,pady=(10))
        self.type_event_label.config(anchor=E)
         
        self.type_event = ttk.Combobox(frame, width=32,values=["Private event","Select type of event*","Business event"])
        self.type_event.grid(row=3,column=1,pady=(10))
        self.type_event.current(1)

        self.startDate_label=Label(frame, text="Start date:", bg='white',width=12,font='ansi 10 ')
        self.startDate_label.grid(row=4, column=0,pady=(10))
        self.startDate_label.config(anchor=E)
        
        self.calendar_icon = PhotoImage(file="CalendarIcon.png", width=20, height=20)
        self.startDate_calendar_button = Button(frame, width=20, height=20,image=self.calendar_icon,bg='white',highlightthickness=0,bd=0,command=date_picker_popup)
        self.startDate_calendar_button.grid(row=4, column=1,sticky=E)

        self.startDate = Entry(frame, bd=1, width=25, font='ansi 10',borderwidth=2,highlightbackground='black')
        self.startDate.grid(row=4, column=1, pady=(10),sticky=W)

        self.finishDate_label=Label(frame, text="Finish date:", bg='white',width=12,font='ansi 10 ')
        self.finishDate_label.grid(row=5, column=0,pady=(10))
        self.finishDate_label.config(anchor=E)

        self.finishDate = Entry(frame, bd=1, width=25, font='ansi 10',borderwidth=2,highlightbackground='black')
        self.finishDate.grid(row=5, column=1, pady=(10),sticky=W)

        self.finishDate_calendar_button = Button(frame, width=20, height=20,image=self.calendar_icon,bg='white',highlightthickness=0,bd=0,command=date_picker_popup)
        self.finishDate_calendar_button.grid(row=5, column=1,sticky=E)

        self.startTime_label=Label(frame, text="Start time:", bg='white',width=12,font='ansi 10 ')
        self.startTime_label.grid(row=6, column=0,pady=(10))
        self.startTime_label.config(anchor=E)

        self.clock_icon = PhotoImage(file="ClockIcon.png", width=20, height=20)
        self.startTime_clock_button = Button(frame, width=20, height=20,image=self.clock_icon,bg='white',highlightthickness=0,bd=0,command=time_picker_popup)
        self.startTime_clock_button.grid(row=6, column=1,sticky=E)

        self.startTime = Entry(frame, bd=1, width=25, font='ansi 10',borderwidth=2,highlightbackground='black')
        self.startTime.grid(row=6, column=1, pady=(10),sticky=W)

        self.FinishTime_label=Label(frame, text="Finish time:", bg='white',width=12,font='ansi 10 ')
        self.FinishTime_label.grid(row=7, column=0,pady=(10))
        self.FinishTime_label.config(anchor=E)

        self.FinishTime = Entry(frame, bd=1, width=25, font='ansi 10',borderwidth=2,highlightbackground='black')
        self.FinishTime.grid(row=7, column=1, pady=(10),sticky=W)

        self.FinishTime_clock_button = Button(frame, width=20, height=20,image=self.clock_icon,bg='white',highlightthickness=0,bd=0,command=time_picker_popup)
        self.FinishTime_clock_button.grid(row=7, column=1,sticky=E)

        self.OKButton=Button(frame2, width=8, height=1, text='OK',bg='#db124b',fg='white',font='ansi 10 underline')
        self.OKButton.grid(row=1,column=4)

        def delete_messageWindow():
            win = Toplevel()
            win.title('Warning')
            win.geometry("330x150")
            win.resizable(0,0)
            win.config(bg='white')

            self.warning_icon = PhotoImage(file="WarningIcon.png")
            self.icon_label=Label(win,image=self.warning_icon,height=50,width=50,borderwidth=0,bg='white')
            self.icon_label.grid(row=1,column=1,pady=10,padx=13)
            

            label=Label(win, text="Are you sure you want to delete?",bg='white',font='ansi 11 bold')
            label.grid(row=1,column=2)
            
            label2=Label(win, text="If you delete now this event won't be saved.",bg='white')
            label2.grid(row=2,column=2)

            frame=Frame(win,width=200,height=25)
            frame.place(x=170,y=110)
            frame.config(bg='white')

            def delete_button():
                win.destroy()
                master.destroy()
            
            delete_button=Button(frame, text='Delete', command=delete_button,bg='#db124b',fg='white',font='ansi 10 underline')
            delete_button.grid(row=3,column=2,ipadx=8,padx=8,sticky=W)

            cancel_button=Button(frame, text='Cancel', command=win.destroy,bg='#F04979',fg='white',font='ansi 10')
            cancel_button.grid(row=3,column=1,ipadx=8)
    
        self.DeleteButton=Button(frame2, width=8, height=1, text='Delete',bg='#F04979',fg='white',font='ansi 10',command=delete_messageWindow)
        self.DeleteButton.grid(row=1,column=2)

        fill_label=Label(frame2,text='',width=14,bg='white')
        fill_label.grid(row=1,column=1)

        fill_label2=Label(frame2,text='',width=1,bg='white')
        fill_label2.grid(row=1,column=3)


    def _backspace(self, entry):
        cont = entry.get()
        entry.delete(0, END)
        entry.insert(0, cont[:-1])

    def _check(self, index, size):
        entry = self.entries[index]
        next_index = index + 1
        next_entry = self.entries[next_index] if next_index < len(self.entries) else None
        data = entry.get()

        if len(data) > size or not data.isdigit():
            self._backspace(entry)
        if len(data) >= size and next_entry:
            next_entry.focus()


root = Tk()
root.title("New Event")
root.geometry("365x415")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
                



                

