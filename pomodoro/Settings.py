import customtkinter as ctk
from TimeSelector import *
from typing import Optional,Union,Tuple
from PIL import Image
from ActionButtons import *
from SlidTimeSelection import *
class SettingWindow(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None,returnArray=[0,0,0,0], **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)


        # self._user_input: Union[str, None] = None
        self.returnArray = returnArray
        counter = 0
        for i in self.returnArray:
            if i < 10:
                self.returnArray[counter] = '0'+ str(self.returnArray[counter])
            else:
                self.returnArray[counter] = str(self.returnArray[counter])
            counter+=1
        self.resizable(False,False)
        self.geometry('300x350')
        self.overrideredirect(False)
        ##BG
        img = Image.open("images\\BGconfig1.png")
        img = ctk.CTkImage(img,size=(300,350))
        self.labelBg = ctk.CTkLabel(self,image=img,text='',width=300,height=350)
        self.labelBg.place(x=0,y=0)
        
        ##button
        self.submitButton = ctk.CTkButton(self,width=50,height=50,command=self.submitAction, text=' Submit ',font=('Minecraft', 20),fg_color='gray',corner_radius=0,border_width=3,border_color='#999EA3')
        self.submitButton.place(x=100,y=290)
        
        ##timeSelection
        #study
        self.secStudySelection = TimeSelector(self)
        self.secStudySelection.text.set(str(self.returnArray[0]))
        self.secStudySelection.posX=-180
        self.secStudySelection.place(x=self.secStudySelection.posX*-1, y=self.secStudySelection.posY*-1)
        self.minStudySelection = TimeSelector(self)
        self.minStudySelection.text.set(str(self.returnArray[1]))
        self.minStudySelection.place(x=self.minStudySelection.posX*-1, y=self.minStudySelection.posY*-1)
        #relax
        self.secRelaxSelection = TimeSelector(self)
        self.secRelaxSelection.text.set(str(self.returnArray[2]))
        self.secRelaxSelection.posX=-180
        self.secRelaxSelection.posY=-200
        self.secRelaxSelection.place(x=self.secRelaxSelection.posX*-1, y=self.secRelaxSelection.posY*-1)
        self.minRelaxSelection = TimeSelector(self)
        self.minRelaxSelection.text.set(str(self.returnArray[3]))
        self.minRelaxSelection.posY=-200
        self.minRelaxSelection.place(x=self.minRelaxSelection.posX*-1, y=self.minRelaxSelection.posY*-1)
        ##label Study
        self.frameStudy = customtkinter.CTkFrame(self,width=100,height=40,corner_radius=0,border_width=0)
        self.frameStudy.place(x=100,y=10)
        self.labelStudy = customtkinter.CTkLabel(self.frameStudy, image=img,text='Study',font=('Minecraft',25))
        self.labelStudy.place(x=-100,y=-155)
        ##Label Relax
        self.frameRelax = customtkinter.CTkFrame(self,width=100,height=40,corner_radius=0,border_width=0)
        self.frameRelax.place(x=100,y=150)
        self.labelRelax = customtkinter.CTkLabel(self.frameRelax, image=img,text='Relax',font=('Minecraft',25))
        self.labelRelax.place(x=-100,y=-155)

    def submitAction(self):
        self.returnArray = [self.secStudySelection.text.get(),self.minStudySelection.text.get(),self.secRelaxSelection.text.get(),self.minRelaxSelection.text.get()]
        self.destroy()
        return 

    
    def get_input(self): ##
        self.master.wait_window(self)
        
        return self.returnArray
    
    def set_returnArray(self,value):
        self.returnArray = value
