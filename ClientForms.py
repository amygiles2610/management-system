from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import subprocess

class main:
    def __init__(self,master):
        self.master = master
        
        def raise_frame(frame):
            frame.tkraise()

        top_frame=Frame(master)
        top_frame.config(bg='white')
        top_frame.grid(row=1,column=1)
        top_frame.place(x=20,y=50)

        self.label_1=Label(top_frame, text='Client details',font='ansi 12 bold',bg='white')
        self.label_1.grid(row=0,column=0)

        self.label_2=Label(top_frame, text='Delivery dates',font='ansi 12',bg='white')
        self.label_2.grid(row=0,column=1)

        self.label_3=Label(top_frame, text='Project details',font='ansi 12',bg='white')
        self.label_3.grid(row=0,column=2)

        self.label_4=Label(top_frame, text='Downloads info',font='ansi 12',bg='white')
        self.label_4.grid(row=0,column=3)

        self.label_5=Label(top_frame, text='Audio and creative assets',font='ansi 12',bg='white')
        self.label_5.grid(row=0,column=4)

        self.label_6=Label(top_frame, text='Other requirements',font='ansi 12',bg='white')
        self.label_6.grid(row=0,column=5)

        client_details_page = Frame(master)
        client_details_page.config(bg='white')

        delivery_dates_page = Frame(master)
        delivery_dates_page.config(bg='white')

        project_details_page = Frame(master)
        project_details_page.config(bg='white')

        downloads_info_page = Frame(master)
        downloads_info_page.config(bg='white')

        creative_assets_page = Frame(master)
        creative_assets_page.config(bg='white')

        creative_assets_2page = Frame(master)
        creative_assets_2page.config(bg='white')

        for frame in (client_details_page, delivery_dates_page,project_details_page,downloads_info_page,creative_assets_page,creative_assets_2page):
            frame.grid(row=0, column=0,sticky='nesw',padx=150,pady=150)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure("pink.Horizontal.TProgressbar", foreground='white', background='#db124b',troughcolor='white')

        self.progressbar=ttk.Progressbar(top_frame,style="pink.Horizontal.TProgressbar",orient="horizontal",length=950,mode="determinate")
        self.progressbar.grid(row=2,column=0,columnspan=6,pady=5)
        self.progress_value=12.5
        self.progressbar["value"]=self.progress_value

        def CD_forward_button_control():
            self.progress_value=self.progress_value + 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(delivery_dates_page)

        self.CDsub_section_label=Label(client_details_page,text='Company details',font='ansi 20 bold',bg='white')
        self.CDsub_section_label.grid(row=1,column=1)

        self.CDentry1_label=Label(client_details_page,text='Client name:',font='ansi 15',bg='white')
        self.CDentry1_label.grid(row=2,column=1)

        self.CDentry1=Entry(client_details_page)
        self.CDentry1.grid(row=2,column=2)

        self.CDentry2_label=Label(client_details_page,text='Record label:',font='ansi 15',bg='white')
        self.CDentry2_label.grid(row=3,column=1)

        self.CDentry2=Entry(client_details_page)
        self.CDentry2.grid(row=3,column=2)

        self.CDentry3_label=Label(client_details_page,text='Music group:',font='ansi 15',bg='white')
        self.CDentry3_label.grid(row=4,column=1)
    
        self.CDentry3=Entry(client_details_page)
        self.CDentry3.grid(row=4,column=2)

        self.CDbutton=Button(client_details_page,text='Proceed',command=CD_forward_button_control)
        self.CDbutton.grid(row=5,column=1)


        def DD_back_button_control():
            self.progress_value=self.progress_value - 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(client_details_page)
        def DD_forward_button_control():
            self.progress_value=self.progress_value + 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(project_details_page)
    

        self.DDsub_section_label=Label(delivery_dates_page,text='Delivery Dates',font='ansi 12 bold')
        self.DDsub_section_label.grid(row=1,column=1)

        self.DDentry1_label=Label(delivery_dates_page,text='Poject go live date:',font='ansi 10',bg='white')
        self.DDentry1_label.grid(row=2,column=1)

        self.DDentry1=Entry(delivery_dates_page)
        self.DDentry1.grid(row=2,column=2)

        self.DDentry2_label=Label(delivery_dates_page,text='Sign off/Approval date::',font='ansi 10',bg='white')
        self.DDentry2_label.grid(row=3,column=1)

        self.DDentry2=Entry(delivery_dates_page)
        self.DDentry2.grid(row=3,column=2)

        self.DDentry3_label=Label(delivery_dates_page,text='Assets delivery date:',font='ansi 10',bg='white')
        self.DDentry3_label.grid(row=4,column=1)

        self.DDentry3=Entry(delivery_dates_page)
        self.DDentry3.grid(row=4,column=2)

        self.DDentry4_label=Label(delivery_dates_page,text='Audio files delivery date:',font='ansi 10',bg='white')
        self.DDentry4_label.grid(row=5,column=1)
    
        self.DDentry4=Entry(delivery_dates_page)
        self.DDentry4.grid(row=5,column=2)

        self.DDbutton1=Button(delivery_dates_page,text='Back',command=DD_back_button_control)
        self.DDbutton1.grid(row=6,column=1)

        self.DDbutton2=Button(delivery_dates_page,text='Proceed',command=DD_forward_button_control)
        self.DDbutton2.grid(row=6,column=2)

        def PD_back_button_control():
            self.progress_value=self.progress_value - 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(delivery_dates_page)
        def PD_forward_button_control():
            self.progress_value=self.progress_value + 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(downloads_info_page)

        self.PDsub_section_label=Label(project_details_page,text='Project Details',font='ansi 12 bold')
        self.PDsub_section_label.grid(row=1,column=1,sticky=W)

        self.PDentry1_label=Label(project_details_page,text='Artist/Band name:',font='ansi 10',bg='white')
        self.PDentry1_label.grid(row=2,column=1,sticky=W)

        self.PDentry1=Entry(project_details_page)
        self.PDentry1.grid(row=2,column=1)

        self.PDlabel1=Label(project_details_page,text='Release type', font='ansi 11 bold',bg='white')
        self.PDlabel1.grid(row=3,column=1,sticky=W)

        self.PDlabel2=Label(project_details_page,text='TICK ALL RELEVANT BOXES', font='ansi 11 italic',bg='white')
        self.PDlabel2.grid(row=4,column=1,sticky=W)
        
        var1 = IntVar()
        self.PDcheckbox1 = Checkbutton(project_details_page, text="Compilation", variable=var1,bg='white',font='ansi 10')
        self.PDcheckbox1.grid(row=5,column=2,sticky=W)

        var2 = IntVar()
        self.PDcheckbox2 = Checkbutton(project_details_page, text="Boxset", variable=var2,bg='white',font='ansi 10')
        self.PDcheckbox2.grid(row=6,column=2,sticky=W)

        var3 = IntVar()
        self.PDcheckbox3 = Checkbutton(project_details_page, text="Album", variable=var3,bg='white',font='ansi 10')
        self.PDcheckbox3.grid(row=7,column=2,sticky=W)

        var4 = IntVar()
        self.PDcheckbox4 = Checkbutton(project_details_page, text="Single/EP", variable=var4,bg='white',font='ansi 10')
        self.PDcheckbox4.grid(row=8,column=2,sticky=W)

        var5 = IntVar()
        self.PDcheckbox5 = Checkbutton(project_details_page, text="Bonus track", variable=var5,bg='white',font='ansi 10')
        self.PDcheckbox5.grid(row=9,column=2,sticky=W)

        var6 = IntVar()
        self.PDcheckbox6 = Checkbutton(project_details_page, text="Other", variable=var6,bg='white',font='ansi 10')
        self.PDcheckbox6.grid(row=10,column=2,sticky=W)

        self.PDentry2=Entry(project_details_page)
        self.PDentry2.grid(row=10,column=3)

        self.PDbutton1=Button(project_details_page,text='Back',command=PD_back_button_control)
        self.PDbutton1.grid(row=11,column=3)

        self.PDbutton2=Button(project_details_page,text='Proceed',command=PD_forward_button_control)
        self.PDbutton2.grid(row=11,column=4)

        def DI_back_button_control():
            self.progress_value=self.progress_value - 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(project_details_page)
        def DI_forward_button_control():
            self.progress_value=self.progress_value + 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(creative_assets_page)

        self.DIsub_section_label=Label(downloads_info_page,text='Downloads type',font='ansi 12 bold')
        self.DIsub_section_label.grid(row=1,column=1,sticky=W)

        self.DIentry1_label=Label(downloads_info_page,text='Confirm number of unique downloads:',font='ansi 10',bg='white')
        self.DIentry1_label.grid(row=2,column=1)

        self.DIentry1=Entry(downloads_info_page)
        self.DIentry1.grid(row=2,column=2)

        self.DIlabel1=Label(downloads_info_page,text='TICK ALL RELEVANT BOXES', font='ansi 11 italic',bg='white')
        self.DIlabel1.grid(row=3,column=1)

        self.DIlabel2=Label(downloads_info_page,text='These will be used to name the audio', font='ansi 11 italic bold',bg='white')
        self.DIlabel2.grid(row=3,column=2,sticky=E)

        var1 = IntVar()
        self.DIcheckbox1 = Checkbutton(downloads_info_page, text="Single reedemable download code for a single download", variable=var1,bg='white',font='ansi 10')
        self.DIcheckbox1.grid(row=4,column=2,sticky=W)
        
        var2 = IntVar()
        self.DIcheckbox2 = Checkbutton(downloads_info_page, text="Single reedemable download code for multiple downloads", variable=var2,bg='white',font='ansi 10')
        self.DIcheckbox2.grid(row=5,column=2,sticky=W)

        var3 = IntVar()
        self.DIcheckbox3 = Checkbutton(downloads_info_page, text="Multiple reedemable download codes for a multiple downloads",variable=var3,bg='white',font='ansi 10')
        self.DIcheckbox3.grid(row=6,column=2,sticky=W)

        self.DIbutton1=Button(downloads_info_page,text='Back',command=DI_back_button_control)
        self.DIbutton1.grid(row=7,column=3)

        self.DIbutton2=Button(downloads_info_page,text='Proceed',command=DI_forward_button_control)
        self.DIbutton2.grid(row=7,column=4)


        def CA_back_button_control():
            self.progress_value=self.progress_value - 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(downloads_info_page)
        def CA_forward_button_control():
            self.progress_value=self.progress_value + 12.5
            self.progressbar["value"] = self.progress_value
            return raise_frame(creative_assets_2page)

        self.CAsub_section_label=Label(creative_assets_page,text='Audio file formats',font='ansi 12 bold')
        self.CAsub_section_label.grid(row=1,column=1,sticky=W)

        self.CAlabel1=Label(creative_assets_page,text='TICK ALL RELEVANT BOXES', font='ansi 11 italic',bg='white')
        self.CAlabel1.grid(row=2,column=1,sticky=W)

        var1 = IntVar()
        self.CAcheckbox1 = Checkbutton(creative_assets_page, text="WAC", variable=var1,bg='white',font='ansi 10')
        self.CAcheckbox1.grid(row=3,column=2,sticky=W)
        
        var2 = IntVar()
        self.CAcheckbox2 = Checkbutton(creative_assets_page, text="MP3", variable=var2,bg='white',font='ansi 10')
        self.CAcheckbox2.grid(row=4,column=2,sticky=W)

        var3 = IntVar()
        self.CAcheckbox3 = Checkbutton(creative_assets_page, text="Other",variable=var3,bg='white',font='ansi 10')
        self.CAcheckbox3.grid(row=5,column=2,sticky=W)

        self.CAentry1=Entry(creative_assets_page)
        self.CAentry1.grid(row=5,column=3)

        self.CAlabel2=Label(creative_assets_page,wraplength=800,text='If different audio formats for different releases are required please list which downloads require which formats below. Otherwise it will be assumed that all downloads are to be delivered in all file formarts that are checked in the list above', font='ansi 11 italic',bg='white')
        self.CAlabel2.grid(row=6,column=1,columnspan=5,sticky=W)
        
        self.CAlabel1=Label(creative_assets_page,text='Special audio file requirements:', font='ansi 11 italic',bg='white')
        self.CAlabel1.grid(row=7,column=1,sticky=W)

        self.CAentry2=Entry(creative_assets_page)
        self.CAentry2.grid(row=7,column=2)

        self.CAbutton1=Button(creative_assets_page,text='Back',command=CA_back_button_control)
        self.CAbutton1.grid(row=8,column=3)

        self.CAbutton2=Button(creative_assets_page,text='Proceed',command=CA_forward_button_control)
        self.CAbutton2.grid(row=8,column=4)
        



        raise_frame(client_details_page)


root = Tk()
root.title("Client Forms")
root.geometry("1000x600")
root.resizable(0,0)
root.configure(bg='white')
main(root)
root.mainloop()
