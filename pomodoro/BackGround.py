from typing import Optional, Tuple, Union, Any
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
class BackGroud(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 400, height: int = 680, corner_radius: Optional[Union[int, str]] = None, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = None, border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.place(x=0,y=0)
        #BG
        # image = tk.PhotoImage(file="images\\BGteste2.png")
        # image = image.subsample(1,1)
        image = ctk.CTkImage(Image.open('images\\BGteste2.png'),size=(400,680))
        print(image)
        imageLabel = ctk.CTkLabel(self,image=image, text= '')
        imageLabel.place(x=0,y=0)


# from typing import Optional, Tuple, Union
# import customtkinter as ctk
# import tkinter as tk

# class BackGroud(ctk.CTkFrame):
#     def __init__(self, master: any, width: int = 400, height: int = 680, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
#         super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
#         #BG
#         image = tk.PhotoImage(file="images/BGteste2.png")
#         imageLabel = ctk.CTkLabel(self,image=image, text= ' ')
#         imageLabel.place(x=0,y=0)
