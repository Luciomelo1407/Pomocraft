import customtkinter
from typing import Union, Optional, Type, Any, Tuple
from customtkinter import CTkImage
from customtkinter import CTkFont

class SlidTimeSelection(customtkinter.CTkFrame):
    def __init__(self, master: Any, width: int = 50, height: int = 50, corner_radius: Optional[Union[int, str]] = None, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = None, border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)   
        self.text = customtkinter.StringVar()
        self.text.set('0')
        self.configure(fg_color='transparent',border_width=0)
        ##EntryPoint
        self.box = customtkinter.CTkEntry(self,text_color='white',textvariable=self.text,fg_color='gray',state='disable',width=50,font=('Minecraft', 15)) #por enquanto desativado dps bota
        self.box.place(x=10,y=10)
        ##Button
        self.incrementButton = customtkinter.CTkButton(self,command=self.incrementValue,width=15,height=15,text='',corner_radius=0)
        self.incrementButton.place(x=40,y=10)
        self.decrecimentButton = customtkinter.CTkButton(self,command=self.decrecimentValue,width=15,height=15,text='',corner_radius=0,border_width=1,border_spacing=0,border_color='black',fg_color='gray')
        self.decrecimentButton.place(x = 40, y=24)
    
    def incrementValue(self):
        texto = self.text.get()
        texto = int(texto)
        texto +=1
        texto = str(texto)
        self.text.set(texto)
    def decrecimentValue(self):
        texto = self.text.get()
        texto = int(texto)
        texto -=1
        texto = str(texto)
        self.text.set(texto)

# def main():
#     root = customtkinter.CTk()
#     root.geometry('300x300')
#     label = SlidTimeSelection(root)
#     label.place(x=50,y=50)
#     root.mainloop()
#     pass

# main()
