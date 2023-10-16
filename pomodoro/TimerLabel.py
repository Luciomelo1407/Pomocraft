from typing import Optional, Tuple, Union
import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class TimerLabel(ctk.CTkLabel):
    def __init__(self, master: any, width: int = 0, height: int = 28, corner_radius: int | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, text_color: str | Tuple[str, str] | None = None, text_color_disabled: str | Tuple[str, str] | None = None, text: str = "CTkLabel", font: tuple | CTkFont | None = None, image: CTkImage | None = None, compound: str = "center", anchor: str = "center", wraplength: int = 0, **kwargs):
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color, text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)
        self.configure( font=('Minecraft', 55))
        
        
        # minLabel = TimerLabel(relogin, text=TimeTransform().transform(min))
        # minLabel.place(x=10,y=60)
        # dots = TimerLabel(relogin, text=":")
        # dots.place(x=90,y=53)
        # secLabel = TimerLabel(relogin, text=TimeTransform().transform(sec))
        # secLabel.place(x=110,y=60)