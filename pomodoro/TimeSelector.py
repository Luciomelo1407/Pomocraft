import customtkinter
from typing import Union, Optional, Type, Any, Tuple
from customtkinter import CTkImage
from customtkinter import CTkFont
from customtkinter.windows.widgets import image
from PIL import Image

class TimeSelector(customtkinter.CTkFrame):
    def __init__(self, master: Any, width: int = 68, height: int = 48, corner_radius: Optional[Union[int, str]] = None, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = None, border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)   
        

        self.posX = -55
        self.posY = -60
        self.configure(fg_color='transparent',border_width=0)
        img = customtkinter.CTkImage(Image.open("images\\BGconfig1.png"),size=(300,350))
        bg = customtkinter.CTkLabel(self,text='', image=img,width=300,height=350)
        bg.place(x= self.posX,y=self.posY)
        ##BOx
        self.text = customtkinter.StringVar()
        self.text.set('00')
        self.box = customtkinter.CTkEntry(self,text_color='white',textvariable=self.text,fg_color='gray',state='disable',width=63,height=48,font=('Minecraft', 20)) #por enquanto desativado dps bota
        self.box.place(x=0,y=0)
        ##Button
        self.imgBincrement = customtkinter.CTkImage(Image.open('images\\ButtonUp.jpg'),size=(15,15))
        self.incrementButton = customtkinter.CTkButton(self,command=self.incrementValue,image=self.imgBincrement,width=20,height=20,text='',corner_radius=0,border_width=0,border_spacing=0,border_color='black',fg_color='gray')
        self.incrementButton.place(x=40,y=3)
        self.imgBdecreciment = customtkinter.CTkImage(Image.open('images\\ButtonDown.jpg'),size=(15,15))
        self.decrecimentButton = customtkinter.CTkButton(self,command=self.decrecimentValue,image=self.imgBdecreciment,width=20,height=0,text='',corner_radius=0,border_width=0,border_spacing=0,border_color='black',fg_color='gray')
        self.decrecimentButton.place(x = 40, y=24)
    
    def incrementValue(self):
        texto = self.text.get()
        texto = int(texto)
        texto +=1
        inteiro = texto
        texto = str(texto)
        if inteiro<10:
            texto = '0'+texto
        self.text.set(texto)
    def decrecimentValue(self):
        texto = self.text.get()
        texto = int(texto)
        inteiro = texto
        if not inteiro == 0:
            texto -=1
        texto = str(texto)
        if inteiro <10:
            texto = '0'+texto
        self.text.set(texto)



