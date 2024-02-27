import customtkinter as ctk
from TimeSelector import *
from typing import Optional,Union,Tuple
from PIL import Image
from ActionButtons import *
from SlidTimeSelection import *
import os
class MusicSelectorWin(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry('300x350')
    
        self.musicList = os.listdir(path=r"songs\musics")
        print(self.musicList)

        self.labelBG = customtkinter.CTkLabel(self,image=ctk.CTkImage(Image.open('images\\BGconfig1Darker.png'),size=(300,350)),text='')
        self.labelBG.place(x=0,y=0)
        
        self.listFrameRoot = ctk.CTkScrollableFrame(self,width=290,height=260,border_width=0,corner_radius=0)
        self.listFrameRoot.place(x=5,y=10)
        self.listFrame = ctk.CTkFrame(self.listFrameRoot,width=290, height=400)
        self.listFrame.pack()
        self.listBG = ctk.CTkLabel(self.listFrame,text='', image=ctk.CTkImage(Image.open('images\\BGconfig1.png'),size=(290,260)))
        self.listBG.place(x=0,y=0)
        posX = 0
        posY = 0
        
        self.lableTeste = customtkinter.CTkLabel(self.listFrame,text="isso é apenas um texte")
        self.lableTeste.place(x=0,y=0)


        self.row = []
        counter = 0
        for i in self.musicList:
            print(posY)
            self.row.append(customtkinter.CTkLabel(self.listFrame,text=i))
            self.row[counter].place(x=posX,y=posY)
            posY+=25
            counter+=1
        # 

