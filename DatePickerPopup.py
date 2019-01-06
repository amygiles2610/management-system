import calendar
import datetime
from tkinter import *
from tkinter import messagebox
import subprocess

class Calendar:
    def __init__(self, master, values={}):
        
        self.master = master
        self.values = values

        self.frame=Frame(master,width=300, height=200, bg='white')
        self.frame.place(relx=0.5, rely=0.5, anchor=E,x=90,y=5)
        
        self.cal = calendar.TextCalendar(calendar.MONDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.day = datetime.date.today().day

        self.wid = []
        self.day_selected = 1
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''
        
        self.setup(self.year, self.month)
        
    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            self.wid.remove(w)

    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1

        self.clear()
        self.setup(self.year, self.month)
 
    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1

        self.clear()
        self.setup(self.year, self.month)

    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name
         

        self.values['day_selected'] = day
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = name
        self.values['month_name'] = calendar.month_name[self.month_selected]

        self.clear()
        self.setup(self.year, self.month)

    def setup(self, y, m):
        
        self.left = Button(self.frame, text='<', command=self.go_prev,bg='#db124b',fg='white')
        self.wid.append(self.left)
        self.left.grid(row=0, column=1)
         
        self.header = Label(self.frame, height=2, bg='white', text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(self.header)
        self.header.grid(row=0, column=2, columnspan=3)
         
        self.right = Button(self.frame, text='>', command=self.go_next,bg='#db124b',fg='white')
        self.wid.append(self.right)
        self.right.grid(row=0, column=5)
         
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday', ]
        
        for num in range(len(days)):
            name=days[num]
            self.t = Label(self.frame, text=name[:3],bg='white')
            self.wid.append(self.t)
            self.t.grid(row=1, column=num)

        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    if self.day == day and self.month ==datetime.date.today().month and self.year==datetime.date.today().year:
                        self.b = Button(self.frame, width=1,borderwidth=0, text=day,fg='#db124b',bg='pink',activebackground='pink',command= lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                        self.wid.append(self.b)
                        self.b.grid(row=w, column=d)
                    else:
                        self.b = Button(self.frame, width=1,borderwidth=0, text=day,bg='white',activebackground='pink',command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                        self.wid.append(self.b)
                        self.b.grid(row=w, column=d)


        self.ok = Button(self.frame, width=5, text='OK', command=self.worked , bg='#db124b',fg='white')
        self.ok.grid(row=9, column=2, columnspan=3, pady=10)

        def pressed():
            self.b.config(bg='dark pink')

         
    def worked(self):
        messagebox.showinfo('Yey','Succesfully.')


root = Tk()
root.title("Calendar")
root.configure(bg='white')
root.geometry("200x240")
root.resizable(0,0)
Calendar(root)
root.mainloop()
