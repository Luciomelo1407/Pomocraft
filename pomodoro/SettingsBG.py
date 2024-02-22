from typing import Optional, Tuple, Union, Any
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

class SettingsBG(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 300, height: int = 350, corner_radius: Optional[Union[int, str]] = None, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = None, border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        #BG

        # img = Image.open('images/BGconfig1.png')
        # img = img.resize((300, 350))
        # imagebg = ctk.CTkImage(img)
        # imageLabel = ctk.CTkLabel(self,image=imagebg)
        # imageLabel.place(x=0,y=0)
