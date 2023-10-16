from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk
from ActionButtons import *

class Settings(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title("configuracoes")
        self.geometry('300x300')
        # fontsize = 25
        # string1a60 = [' 0 ' , ' 1 ' , ' 2 ' , ' 3 ' , ' 4 ' , ' 5 ' , ' 6 ' , ' 7 ' , ' 8 ' , ' 9 ' , ' 10 ' , ' 11 ' , ' 12 ' , ' 13 ' , ' 14 ' , ' 15 ' , ' 16 ' , ' 17 ' , ' 18 ' , ' 19 ' , ' 20 ' , ' 21 ' , ' 22 ' , ' 23 ' , ' 24 ' , ' 25 ' , ' 26 ' , ' 27 ' , ' 28 ' , ' 29 ' , ' 30 ' , ' 31 ' , ' 32 ' , ' 33 ' , ' 34 ' , ' 35 ' , ' 36 ' , ' 37 ' , ' 38 ' , ' 39 ' , ' 40 ' , ' 41 ' , ' 42 ' , ' 43 ' , ' 44 ' , ' 45 ' , ' 46 ' , ' 47 ' , ' 48 ' , ' 49 ' , ' 50 ' , ' 51 ' , ' 52 ' , ' 53 ' , ' 54 ' , ' 55 ' , ' 56 ' , ' 57 ' , ' 58 ' , ' 59 ' , '60']
        # bg = tk.PhotoImage(file='images/BGconfig1.png')
        # frameBG = ctk.CTkFrame(self,300,300)
        # frameBG.place(x=0,y=0)
        # labelBG = ctk.CTkLabel(frameBG,300,300,text=' ',image=bg)
        # labelBG.place(x=0,y=0)
        # minuteSelection = ctk.CTkComboBox(frameBG,85,30,values=string1a60,dropdown_fg_color='#6f6f6f',fg_color='#6f6f6f',font=('Minecraft', fontsize))
        # minuteSelection.place(x=60,y=60)
        # secondsSelection = ctk.CTkComboBox(frameBG,85,30,values=string1a60,dropdown_fg_color='#6f6f6f',fg_color='#6f6f6f',font=('Minecraft', fontsize))
        # secondsSelection.place(x=150,y=60)
        # studylabel = tk.PhotoImage(file='images/StudySettings.png', width=146,height=38)
        # minutesSelectionLabel = ctk.CTkLabel(frameBG,image=studylabel,text=' ')
        # minutesSelectionLabel.place(x=75,y=10)
        # relaxlabel = tk.PhotoImage(file='images/RelaxSetting.png', width=139,height=38)
        # relaxSelectionLabel = ctk.CTkLabel(frameBG,image=relaxlabel,text=' ')
        # relaxSelectionLabel.place(x=75,y=125)
        # relaxminuteSelection = ctk.CTkComboBox(frameBG,85,30,values=string1a60,dropdown_fg_color='#6f6f6f',fg_color='#6f6f6f',font=('Minecraft', fontsize))
        # relaxminuteSelection.place(x=60,y=180)
        # relaxsecondsSelection = ctk.CTkComboBox(frameBG,85,30,values=string1a60,dropdown_fg_color='#6f6f6f',fg_color='#6f6f6f',font=('Minecraft', fontsize))
        # relaxsecondsSelection.place(x=150,y=180)
        # submit = ActionButtons(frameBG,text="submit", command= lambda: end())
        # submit.place(x=75,y=230)

        # def end():
        #     print(minuteSelection.get('values'))
        #     return 
        