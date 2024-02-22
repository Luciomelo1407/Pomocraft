import customtkinter as ctk
from typing import Optional,Union,Tuple
from PIL import Image
from ActionButtons import *
class SettingWindow(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.resizable(False,False)
        self.geometry('300x350')
        self.overrideredirect(True)
        
        ##BG
        img = Image.open("images\\BGconfig1.png")
        img = ctk.CTkImage(img,size=(300,350))
        self.labelBg = ctk.CTkLabel(self,image=img,text='',width=300,height=350)
        self.labelBg.place(x=0,y=0)
        
        ##button
        self.submitButton = ctk.CTkButton(self,width=50,height=50,command=self.submitAction)
        self.submitButton.place(x=50,y=50)
        
        ##timeSelection

    def submitAction(self):
        self.destroy()

