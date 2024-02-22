import customtkinter
from BackGround import *
from Headder import *
from Settings import *
from Headder import *
from ActionButtons import *
from TimerLabel import *
from TimeTransform import *
from PIL import Image, ImageTk
import pygame

class Pomodoro(customtkinter.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        #atributos de tempo
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
    
    def openSettings(self,event):
        settingsWindow = SettingWindow(self)
        settingsWindow.mainloop()
        return
        
    
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
        else:
            self.secLabel.configure(text=TimeTransform().transform(self.secRelax))
            self.minLabel.configure(text=TimeTransform().transform(self.minRelax))

    def skip(self):
        if self.study:
            self.study = False
            self.secLabel.configure(text=TimeTransform().transform(self.secRelax))
            self.minLabel.configure(text=TimeTransform().transform(self.minRelax))
        else:
            self.study = True
            self.secLabel.configure(text=TimeTransform().transform(self.secStudy))
            self.minLabel.configure(text=TimeTransform().transform(self.minStudy))

        self.running = False
        self.startPause.configure(text='Start',command=self.start)
        

    def pause(self):
        self.running = False
        self.startPause.configure(text='Continue')
        self.startPause.configure(command=self.continueTick)
        return self.timetick()
    
    def continueTick(self):
        if self.running:
            return self.pause()
        else:
            self.startPause.configure(text='Pause')
            self.running = True
            return self.timetick()

    def start(self):
        print("Apertou")
        if self.study:
            self.secRunning = self.secStudy
            self.minRunning = self.minStudy
        else:
            self.secRunning = self.secRelax
            self.minRunning = self.minRelax
        self.running = True
        self.startPause.configure(text='Pause')
        self.startPause.configure(command=self.continueTick)
        return self.timetick()
        
    
    def timetick(self):
        if self.running:
            if not self.secRunning:
                self.minRunning = self.minRunning - 1
                self.minRunning = self.minRunning % 60
            self.secRunning = self.secRunning - 1
            self.secRunning = self.secRunning % 60
            self.secLabel.configure(text=TimeTransform().transform(self.secRunning))
            self.minLabel.configure(text=TimeTransform().transform(self.minRunning))
            print(self.secRunning,self.minRunning)
            self.after(1000, self.timetick)
        return
