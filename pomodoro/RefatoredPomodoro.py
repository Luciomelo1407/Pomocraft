import customtkinter
from winotify import Notification
from BackGround import *
from Headder import *
from Settings import *
from Headder import *
from ActionButtons import *
from TimerLabel import *
from TimeTransform import *
from PIL import Image, ImageTk
import pygame
import os
from MusiSelectorwin import *
import random

class Pomodoro(customtkinter.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        # 
        # self.notificacaoStudy = Notification(app_id="Pomocraft",title="Começando estudos",icon=r'C:\Users\lucio\OneDrive\Área de Trabalho\Lucio\Estudos\Pomocraft\pomodoro\images\icone.ico')
        # self.endOfRelaxNotify = Notification(app_id="Pomocraft",title="Cabo a brincadeira Hora de Estudar",icon=r'C:\Users\lucio\OneDrive\Área de Trabalho\Lucio\Estudos\Pomocraft\pomodoro\images\icone.ico')
        # self.endOfStudy = Notification(app_id="Pomocraft",title="Já pode dencansar",icon=r'C:\Users\lucio\OneDrive\Área de Trabalho\Lucio\Estudos\Pomocraft\pomodoro\images\icone.ico')
        pathAtual = os.getcwd()
        pathAtual.replace('\\','\\\\')
        self.notificacaoStudy = Notification(app_id="Pomocraft",title="Começando estudos",icon= pathAtual +'\\'+ 'images\\icone.ico')
        self.endOfRelaxNotify = Notification(app_id="Pomocraft",title="Cabo a brincadeira Hora de Estudar",icon= pathAtual + 'images\\icone.ico')
        self.endOfStudy = Notification(app_id="Pomocraft",title="Já pode dencansar",icon= pathAtual + 'images\\icone.ico')


        pygame.mixer.init()
        pygame.init()
        self.volume = 1

        self.nextLevel = pygame.mixer.Sound("songs\\soundEfects\\Som de XP Minecraft.wav")
        self.nextLevel.set_volume(0.2)
        self.endOfRelax = pygame.mixer.Sound("songs\\soundEfects\\Minecraft Creeper Explosion.wav")
        self.endOfRelax.set_volume(0.2)

        #atributos de tempo
        self.muteFlag = False
        self.study = True;
        self.running = False
        self.secStudy = 0
        self.minStudy = 25
        self.secRelax = 0
        self.minRelax = 5
        self.secRunning = self.secStudy
        self.minRunning = self.minStudy

        #window screen position
        self.resizable(False,False)
        largura = 400
        altura = 680
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenmmheight()
        posix = largura_tela/2 - largura/2
        posiy = altura_tela/2 - altura/7
        self.geometry("%dx%d+%d+%d" % (largura,altura, posix, posiy))
        self.geometry("%dx%d+%d+%d" % (largura,altura,posix,posiy))
        self.title('Pomocraft')
        self.iconbitmap('images\\icone.ico')

        #setupBackground
        backGround = BackGroud(self)
        backGround.place(x=0,y=0)
        customtkinter.CTkInputDialog

        #setUP clock
        self.relogin = ctk.CTkFrame(self,corner_radius=10)
        self.relogin.place(x=100,y=150)
        self.minLabel = TimerLabel(self.relogin, text=TimeTransform().transform(self.minStudy))
        self.minLabel.place(x=10,y=60)
        dots = TimerLabel(self.relogin, text=":")
        dots.place(x=90,y=53)
        self.secLabel = TimerLabel(self.relogin, text=TimeTransform().transform(self.secStudy))
        self.secLabel.place(x=110,y=60)

        #botoes
        self.startPause = ActionButtons(self,text="Start", command=self.start)
        self.startPause.place(x=50,y=400)
        self.resetB = ActionButtons(self,text="Reset",command=self.reset)
        self.resetB.place(x=220,y=400)
        self.skipBTT = ActionButtons(self,text="Skip", command=self.skip)
        self.skipBTT.place(x=125,y=455)

        ##settings
        self.settingsButtonImage = ctk.CTkImage(Image.open("images\\settingsButton.png"),size=(25,25))
        self.settingsButtonImageHoverd = ctk.CTkImage(Image.open("images\\settingsButtonHoverd.png"),size=(25,25))
        self.settingsButton = ctk.CTkLabel(self,image=self.settingsButtonImage, text='', width=25, height=25)
        self.settingsButton.bind('<Enter>',self.on_enter)
        self.settingsButton.bind('<Leave>',self.on_leave)
        self.settingsButton.bind('<Button-1>', self.openSettings)
        self.settingsButton.place(y=650,x=5)
        #headder
        headder = Headder(self,border_width=0,bg_color="transparent",fg_color="transparent",corner_radius=10)

        # self.mute_unmuteImage = tk.PhotoImage(file="images\Botao de mute.png", master=self)
        self.mute_unmuteImage = ctk.CTkImage(Image.open("images\\Botao de mute.png"),size=(40,40))
        # self.mute_unmuteImageHoverd = tk.PhotoImage(file="images\Botao de mute Hoverd.png", master=self)
        self.mute_unmuteImageHoverd = ctk.CTkImage(Image.open("images\\Botao de mute Hoverd.png"),size=(40,40))
        # self.mute_unmuteImageMuted = tk.PhotoImage(file="images\Botao de mute Muted.png",master=self)
        self.mute_unmuteImageMuted = ctk.CTkImage(Image.open("images\\Botao de mute Muted.png"),size=(40,40))
        # self.mute_unmuteImageHoverdMuted = tk.PhotoImage(file='images\Botao de mute Hoverd Muted.png', master=self)
        self.mute_unmuteImageHoverdMuted = ctk.CTkImage(Image.open('images\\Botao de mute Hoverd Muted.png'),size=(40,40))
        self.mute_unmute = ctk.CTkLabel(self, text=' ', image=self.mute_unmuteImage, width=40, height=40)

        self.mute_unmute.bind('<Enter>', self.on_enterMute)
        self.mute_unmute.bind('<Leave>', self.on_leaveMute)
        self.mute_unmute.bind('<Button-1>', self.mute)
        self.mute_unmute.place(x = 50, y = 515)

        self.volumetro = ctk.CTkSlider(self, from_=0, to=1, command=self.slider_event, progress_color='#3b8526',button_color='#6bc349', button_hover_color="#edf5f3", number_of_steps=100)
        self.volumetro.place(x=100, y = 530)

        #musicSelector
        self.musicSelectorImage = ctk.CTkImage(Image.open('images\\musicSelection.png'),size=(25,25))
        self.musicSelectorImageHoverd = ctk.CTkImage(Image.open('images\\musicSelectionHoverd.png'),size=(25,25))
        self.musicSelectorButton = ctk.CTkLabel(self,image=self.musicSelectorImage,text='',corner_radius=0,width=25,height=25)
        self.musicSelectorButton.place(y=650,x=370)
        self.musicSelectorButton.bind('<Enter>',self.on_enterMusic)
        self.musicSelectorButton.bind('<Leave>',self.on_leaveMusic)
        self.musicSelectorButton.bind('<Button-1>',)



    def musicSelectionWindowOpen(self,event):
        musicSelectionWindow = MusicSelectorWin(self)
        musicSelectionWindow.mainloop()
        

    def on_enterMusic(self,event):
        self.musicSelectorButton.configure(image=self.musicSelectorImageHoverd,cursor='hand2')
        pass
    
    def on_leaveMusic(self,event):
        self.musicSelectorButton.configure(image=self.musicSelectorImage)
        pass

    def slider_event(self,value):
            self.volume = value
            if value > 0:
                self.muteFlag = False
                self.mute_unmute.configure(image=self.mute_unmuteImage)
            else:
                self.muteFlag = True
                self.mute_unmute.configure(image=self.mute_unmuteImageMuted)
            pygame.mixer.music.set_volume(value)

    def mute(self, event):
        if not self.muteFlag:
            self.muteFlag = True
            pygame.mixer.music.set_volume(0)
            self.muda()
        else:
            self.muteFlag = False
            pygame.mixer.music.set_volume(self.volume)

    def muda(self):
        self.mute_unmute.configure(image=self.mute_unmuteImageMuted)
        self.mute_unmute.bind('<Leave>', self.on_leaveMute)


    def on_leaveMute(self,event):
        if self.muteFlag:
            self.mute_unmute.configure(image=self.mute_unmuteImageMuted)
        else:
            self.mute_unmute.configure(image=self.mute_unmuteImage)

    def on_enterMute(self,event):
        if self.muteFlag:
            self.mute_unmute.configure(image=self.mute_unmuteImageHoverdMuted,cursor='hand2')
        else:
            self.mute_unmute.configure(image=self.mute_unmuteImageHoverd,cursor='hand2')


    def openSettings(self,event):
        self.pararMusica()
        self.running = False
        self.study = True
        self.settingsButton.unbind('<Button-1>')
        settingsWindow = SettingWindow(self,returnArray=[self.secStudy,self.minStudy,self.secRelax,self.minRelax])
        self.setClockConfig(settingsWindow.get_input())
        settingsWindow.mainloop()
        return

    def setClockConfig(self,retorno):
        if len(retorno) > 0:
            self.secStudy = int(retorno[0])
            self.minStudy = int(retorno[1])
            self.secRelax = int(retorno[2])
            self.minRelax = int(retorno[3])
            self.setClock(self.secStudy,self.minStudy)
        self.settingsButton.bind('<Button-1>',self.openSettings)
        self.startPause.configure(command=self.start)
        self.startPause.configure(text='Start')
        return

    
    def setClock(self, sec, min):
        self.secLabel.configure(text=TimeTransform().transform(sec))
        self.minLabel.configure(text=TimeTransform().transform(min))

    def on_enter(self,event):
        self.settingsButton.configure(image=self.settingsButtonImageHoverd,cursor='hand2')

    def on_leave(self, event):
        self.settingsButton.configure(image=self.settingsButtonImage)

    def reset(self):
        self.running = False
        self.startPause.configure(text='Start',command=self.start)
        if self.study:
            self.secLabel.configure(text=TimeTransform().transform(self.secStudy))
            self.minLabel.configure(text=TimeTransform().transform(self.minStudy))
            self.secRunning = self.secStudy
            self.minRunning = self.minStudy
            self.pararMusica()
        else:
            self.secLabel.configure(text=TimeTransform().transform(self.secRelax))
            self.minLabel.configure(text=TimeTransform().transform(self.minRelax))
            self.secRunning = self.secRelax
            self.minRunning = self.minRelax

    def skip(self):
        if self.study:
            self.study = False
            self.secLabel.configure(text=TimeTransform().transform(self.secRelax))
            self.minLabel.configure(text=TimeTransform().transform(self.minRelax))
            self.pararMusica()
        else:
            self.study = True
            self.secLabel.configure(text=TimeTransform().transform(self.secStudy))
            self.minLabel.configure(text=TimeTransform().transform(self.minStudy))

        self.running = False
        self.startPause.configure(text='Start',command=self.start)
        

    def pause(self):
        self.running = False
        self.pausarMusica()
        self.startPause.configure(text='Continue')
        self.startPause.configure(command=self.continueTick)
        return self.timetick()
    
    def continueTick(self):
        if self.running:
            return self.pause()
        else:
            self.continuarMusica()
            self.startPause.configure(text='Pause')
            self.running = True
            return self.timetick()

    def start(self):
        if self.study:
            self.notificacaoStudy.show()
            self.tocarMucica()
            self.secRunning = self.secStudy
            self.minRunning = self.minStudy
        else:
            self.secRunning = self.secRelax
            self.minRunning = self.minRelax
        self.running = True
        self.startPause.configure(text='Pause')
        self.startPause.configure(command=self.continueTick)
        return self.timetick()
    
    def escolherMusica(self):
        path_music='songs\\musics\\DarkSoulsLofi(enable)'
        dirlist = os.listdir(path=path_music)
        x = random.sample(dirlist,1)
        print(path_music+'\\'+x[0])
        return path_music+'\\'+x[0]
        

    def tocarMucica(self):
        pygame.mixer.music.load(self.escolherMusica())
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        
    
    def pausarMusica(self):
        print("passou aqui")
        pygame.mixer.music.pause()
    
    def continuarMusica(self):
        pygame.mixer.music.unpause()

    def pararMusica(self):
        pygame.mixer.music.stop()
    
    def timetick(self):
        if self.running:
            if not pygame.mixer.music.get_busy() and self.study:
                self.tocarMucica()
            self.setClock(self.secRunning,self.minRunning)
            if not self.secRunning:
                self.minRunning = self.minRunning - 1
                self.minRunning = self.minRunning % 60
            self.secRunning = self.secRunning - 1
            self.secRunning = self.secRunning % 60
            print(self.minRunning,self.secRunning)
            if self.secRunning==0 and self.minRunning == 0:
                if not self.study:
                    self.endOfRelaxNotify.show()
                    self.endOfRelax.play()
                else:
                    self.endOfStudy.show()
                    self.nextLevel.play()
                self.running = False
                self.study = not(self.study)
                self.startPause.configure(text='Continue',command=self.start)
                self.setClock(self.secRunning,self.minRunning)
                self.pararMusica()
                return
            self.after(1000, self.timetick)
        self.setClock(self.secRunning,self.minRunning)
        return
