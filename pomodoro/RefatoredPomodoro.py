import customtkinter
from BackGround import *
from Headder import *
from Settings import *
from Headder import *
from ActionButtons import *
from TimerLabel import *
from TimeTransform import *
import pygame

class Pomodoro(customtkinter.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        #atributos de tempo
        self.running = False
        self.secStudy = 0
        self.minStudy = 25
        self.secRelax = 0
        self.minRelax = 30
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
        #setup Button
        self.settingsButtonImage = tk.PhotoImage(file="images/settingsButton.png", master=self)
        self.settingsButtonImage =self.settingsButtonImage.subsample(1,1)
        self.settingsButtonImageHoverd = tk.PhotoImage(file="images\\settingsButtonHoverd.png", master=self)
        self.settingsButtonImageHoverd =self.settingsButtonImageHoverd.subsample(1,1)
        #setupBackground
        backGround = BackGroud(self)
        
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
        self.settingsButton = ctk.CTkLabel(self,image=self.settingsButtonImage, text=' ', width=25, height=25)
        self.startPause = ActionButtons(self,text="Start", command=self.start)
        self.startPause.place(x=50,y=400)
        self.resetB = ActionButtons(self,text="Reset")
        self.resetB.place(x=220,y=400)
        self.skipBTT = ActionButtons(self,text="Skip")
        self.skipBTT.place(x=125,y=455)

        self.settingsButton.bind('<Enter>')
        self.settingsButton.bind('<Leave>')
        self.settingsButton.bind('<Button-1>')
        self.settingsButton.place(y=650,x=5)

        #headder
        headder = Headder(self,border_width=0,bg_color="transparent",fg_color="transparent",corner_radius=10)
 
    def pause(self):
        self.running = False
        self.startPause.configure(text='Continue')
        return self.timetick()

    def start(self):
        if self.running:
            return self.pause()
        self.running = True
        self.startPause.configure(text='Pause')
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
