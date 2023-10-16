from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk

class Headder(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 400, height: int = 75, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.place(x=0,y=10)
        image = tk.PhotoImage(file='images/titulo2.png')
        textinho = ctk.CTkLabel(self, image=image, text=' ', fg_color="transparent")
        textinho.place(x=2,y=2)
