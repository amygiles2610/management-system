from tkinter import *

class main:                                                                
    def __init__(self, master):
        self.master = master
        
        frame = Frame(master,width=300,height=150)
        frame.place(x=10,y=20)
        frame.config(padx=30,pady=5)
        frame.config(bg='white')
        
        def update_timeText():
            if (self.state):
                self.timer[2] += 1
                if (self.timer[2] >= 100):
                    self.timer[2] = 0
                    self.timer[1] += 1
                if (self.timer[1] >= 60):
                    self.timer[0] += 1
                    self.timer[1] = 0
                self.timeString = self.pattern.format(self.timer[0], self.timer[1], self.timer[2])
                self.timeText.configure(text=self.timeString)
            frame.after(10, update_timeText)

        def start():
            self.state = True

        def pause():
            self.state = False

        def reset():
            self.timer = [0, 0, 0]
            self.timeText.configure(text='00:00:00')

        self.state = False
        self.timer = [0, 0, 0]
        self.pattern = '{0:02d}:{1:02d}:{2:02d}'

        self.timeText = Label(frame, text="00:00:00", font='ansi 30',bg='white')
        self.timeText.grid(row=1,column=1,columnspan=3,pady=50,padx=40)

        self.startButton = Button(frame, text='Start', command=start,font='ansi 10',bg='#db124b',fg='white')
        self.startButton.grid(row=2,column=1,pady=10)

        self.pauseButton = Button(frame, text='Pause', command=pause,font='ansi 10',bg='#db124b',fg='white')
        self.pauseButton.grid(row=2,column=2)

        self.resetButton = Button(frame, text='Reset', command=reset,font='ansi 10',bg='#db124b',fg='white')
        self.resetButton.grid(row=2,column=3)

        update_timeText()

root = Tk()
root.title("Time Tracking")
root.geometry("600x300")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
