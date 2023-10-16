import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x680")

imagemBG = tk.PhotoImage(file="BGteste2.png")
back = tk.Frame(root,width=400,height=680)
bgimsge = tk.Label(back,image=imagemBG)
bgimsge.place(x=0,y=0)
back.place(x=0,y=0)
imageTitle = tk.PhotoImage(file='titulo2.png')
title = tk.Label(back,image=imageTitle)
title.place(x=0,y=0)


root.mainloop()