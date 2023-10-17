import tkinter as tk

import tkinter as tk

def label_click(event):
    label.config(text="Label foi clicada!")

root = tk.Tk()
root.geometry('300x100')

label = tk.Label(root, text='Clique na label!')
label.pack(pady=20)

# Associe o evento de clique do mouse (Button-1) a label_click
label.bind('<Button-1>', label_click)

root.mainloop()