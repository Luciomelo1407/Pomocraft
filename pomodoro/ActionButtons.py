import tkinter
from typing import Any, Callable, Optional, Tuple, Union
import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

        # startStop = ctk.CTkButton(self,text="Start", font=('Minecraft', 40), fg_color='#3b8526', corner_radius=0, border_color='#6bc349', border_width=2, hover_color= "#333333" )
        # startStop.place(x=50,y=400)
        # reset = ctk.CTkButton(self,text="Reset", font=('Minecraft', 40), fg_color='#3b8526', corner_radius=0, border_color='#6bc349', border_width=2, hover_color= "#333333" )
        # reset.place(x=220,y=400)
        # skip = ctk.CTkButton(self,text="Skip", font=('Minecraft', 40), fg_color='#3b8526', corner_radius=0, border_color='#6bc349', border_width=2, hover_color= "#333333" )
        # skip.place(x=125,y=455)


class ActionButtons(ctk.CTkButton):
    def __init__(self, master: any, width: int = 140, height: int = 28, corner_radius: int | None = None, border_width: int | None = None, border_spacing: int = 2, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, hover_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, text_color: str | Tuple[str, str] | None = None, text_color_disabled: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, round_width_to_even_numbers: bool = True, round_height_to_even_numbers: bool = True, text: str = "CTkButton", font: tuple | CTkFont | None = None, textvariable: tkinter.Variable | None = None, image: CTkImage | Any | None = None, state: str = "normal", hover: bool = True, command: Callable[[], None] | None = None, compound: str = "left", anchor: str = "center", **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, border_spacing, bg_color, fg_color, hover_color, border_color, text_color, text_color_disabled, background_corner_colors, round_width_to_even_numbers, round_height_to_even_numbers, text, font, textvariable, image, state, hover, command, compound, anchor, **kwargs)
        self.configure(font=('Minecraft', 30), fg_color='#3b8526', corner_radius=0, border_color='#6bc349', border_width=2, hover_color= "#333333")

