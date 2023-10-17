import pygame
import time
import tkinter as tk
class Sounds:
    def __init__(self) -> None:
        pygame.mixer.init()
        pygame.init()
        volume = 0.5
        
    def tocarEstudo(self):
        pygame.mixer.music.load("songs\musics\Sweden.mp3")
        pygame.mixer.music.play(loops=0)
    def stop():
        print("passou")
        pygame.mixer.stop()

janela = tk.Tk()
janela.geometry('500x500')
pygame.mixer.init()
pygame.init()

def play():
        pygame.mixer.music.load("songs\musics\Sweden.mp3")
        pygame.mixer.music.play(-1)

def funcaoMaluca():
     play()

butao = tk.Button(text='Start', command= lambda: funcaoMaluca())
butao.place(x=50,y=50)
janela.mainloop()