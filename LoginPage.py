from tkinter import *
from tkinter import messagebox
import sqlite3

class main:
    def __init__(self,master):
        self.master = master
        frame = Frame(master, width=400, height=220, bg="white")
        frame.pack(padx=0.5, pady=100, anchor=CENTER)
        
        self.username_label=Label(frame, text="Enter username", bg='white',width=12,font='ansi 10 bold')
        self.username_label.pack(anchor=W)
        
        def on_entry_click_username(event):
            if self.username.get() == 'Username*':
               self.username.delete(0, "end")
               self.username.insert(0, '') 
               self.username.config(fg = 'black')
        def on_focusout_username(event):
            if self.username.get() == '':
                self.username.insert(0, 'Username*')
                self.username.config(fg = 'grey')
        
        self.username = Entry(frame, bd=1, width=30, font='ansi 10')

        self.username.insert(0, 'Username*')
        self.username.bind('<FocusIn>', on_entry_click_username)
        self.username.bind('<FocusOut>', on_focusout_username)

        self.username.config(fg = 'grey')
        self.username.pack(pady=10)
        
        self.username.configure(highlightthickness='0.5')
        self.username.configure(highlightbackground='black')

        self.password=Label(frame, text="Enter password ", bg='white',width=12,font='ansi 10 bold')
        self.password.pack(anchor=W)

        def on_entry_click_password(event):
            if self.password.get() == 'Password*':
               self.password.delete(0, "end")
               self.password.insert(0, '') 
               self.password.config(fg = 'black',show='*')
        def on_focusout_password(event):
            if self.password.get() == '':
                self.password.config(fg = 'grey',show='')
                self.password.insert(0, 'Password*')
        
        self.password = Entry(frame, bd=1,width=30,font='ansi 10')

        self.password.insert(0, 'Password*')
        self.password.bind('<FocusIn>', on_entry_click_password)
        self.password.bind('<FocusOut>', on_focusout_password)

        self.password.config(fg = 'grey')
        self.password.pack(pady=10)
        
        self.password.configure(highlightthickness='0.5')
        self.password.configure(highlightbackground='black')

        self.log_in_button = Button(frame, text="Log in", font='ansi 10', width=26, height=1, fg='white', bg="#db124b", command=self.login)
        self.log_in_button.pack(pady=10)

        self.astrix_label=Label(frame, text="*required fields", bg='white',width=11,font='ansi 8')
        self.astrix_label.pack(anchor=W)
            
    def login(self):
                                            
        with sqlite3.connect("login.db") as db:
                cursor = db.cursor()
        find_user =("SELECT * FROM user WHERE username = ? and password = ?")
        cursor.execute(find_user,[(self.username.get()),(self.password.get())])
        results = cursor.fetchall()

        if results:
            messagebox.showinfo('Yey','Succesfully logged in.')
        else:
            messagebox.showerror('Oops!','Username Not Found.')

    def new_user(self):
    
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
        
        find_user = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(find_user,([self.username.get()]))

        if cursor.fetchall():
            messagebox.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            messagebox.showinfo('Success!','Account Created!')
            self.log()
    
        insertData = """INSERT INTO user(username,firstname,surname,password)
        VALUES(?,?,?,?)"""
        cursor.execute(insertData,[(self.n_username.get()),(self.n_password.get()),(self.firstname.get()),(self.surname.get())])
        db.commit()
    
root = Tk()
root.title("Project Management Log in")
root.geometry("500x400")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
                



                
