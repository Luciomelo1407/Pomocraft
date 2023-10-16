from typing import Optional, Tuple, Union
import customtkinter
from BackGround import *
from Headder import *
from Settings import *
from Headder import *
from ActionButtons import *
from TimerLabel import *
from TimeTransform import *
import time
class Pomodoro(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.resizable(False,False)
        #variables
        largura = 400
        altura = 680
        
        #* Variaveis globais de Tempo
        global minStudy
        global secStudy
        global secRelax
        global minRelax
        secStudy = 0
        minStudy = 5
        secRelax = 0
        minRelax = 3

        #* Variaveis globais de Flag
        global reset
        global runningStudy
        global runningRelax
        global pauseRelax
        global pauseStudy
        reset = False
        runningStudy = False
        runningRelax = False
        pauseRelax = False
        pauseStudy = True

        # resulução do sistema
        larguta_tela = self.winfo_screenwidth()
        altura_tela =  self.winfo_screenmmheight()

        # posicao da tela
        posix = larguta_tela/2 - largura/2
        posiy = altura_tela/2 - altura/7

        # definir a geometry
        self.geometry("%dx%d+%d+%d" % (largura,altura,posix,posiy))
        self.title('Pomocraft')
        backGround = BackGroud(self)
        #headder
        headder = Headder(self,border_width=0,bg_color="transparent",fg_color="transparent",corner_radius=10)
        #settings
        settingsButtonImage = tk.PhotoImage(file="images/settingsButton.png", master=self)
        settingsButtonImage =settingsButtonImage.subsample(1,1)
        
        settingsButton = ctk.CTkButton(self,bg_color='#3b8526', fg_color='#3b8526', image=settingsButtonImage,
                                       corner_radius=0,width=0,height=0,border_spacing=0,border_width=0,text="",
                                       command=lambda: settingsOpen())
        settingsButton.place(y=650,x=5)
        #timerFrame
        relogin = ctk.CTkFrame(self,corner_radius=10)
        relogin.place(x=100,y=150)
        
        #label Timer
        
        minLabel = TimerLabel(relogin, text=TimeTransform().transform(minStudy))
        minLabel.place(x=10,y=60)
        dots = TimerLabel(relogin, text=":")
        dots.place(x=90,y=53)
        secLabel = TimerLabel(relogin, text=TimeTransform().transform(secStudy))
        secLabel.place(x=110,y=60)

        # def (intminLabel._text):
        #     return int(minLabel._text)        
        # def int(secLabel._text):
        #     return int(secLabel._text)
        
        #botoes
        startPause = ActionButtons(self,text="Start",command= lambda: start())
        startPause.place(x=50,y=400)
        resetB = ActionButtons(self,text="Reset", command= lambda: restart())
        resetB.place(x=220,y=400)
        skipBTT = ActionButtons(self,text="Skip", command= lambda: skip())
        skipBTT.place(x=125,y=455)

        

        def settingsOpen():


            global reset
            reset = False
            global runningStudy
            runningStudy = False
            global runningRelax
            runningRelax = False
            global pauseRelax
            pauseRelax = False
            global pauseStudy
            pauseStudy = False
            
            # def combobox_callback_minutes(choice):
            #     print("combobox dropdown clicked:", choice)

            def callback_Study_min(choice):
                global minStudy
                minStudy = int(choice)
                print(choice)
            
            def callback_Study_sec(choice):
                global secStudy
                secStudy = int(choice)
                print(choice)

            def callback_relax_min(choice):
                global minRelax
                minRelax = int(choice)
                print(choice)

            def callback_relax_sec(choice):
                global secRelax
                secRelax = int(choice)
                print(choice)

            def submitgo():
                global runningStudy
                global runningRelax
                global pauseRelax
                global pauseStudy
                print(minStudy, secStudy)
                secLabel.configure(text=TimeTransform().transform(secStudy))
                minLabel.configure(text=TimeTransform().transform(minStudy))
                startPause.configure(text='Start', command=lambda: start())
                attStudy(minStudy, secStudy)
                return settingswindow.destroy()


            settingswindow = Settings()
            fontsize = 25
            string0a60 = [' 0 ' , ' 1 ' , ' 2 ' , ' 3 ' , ' 4 ' , ' 5 ' , ' 6 ' , ' 7 ' , ' 8 ' , ' 9 ' , ' 10 ' , ' 11 ' , ' 12 ' , ' 13 ' , ' 14 ' , ' 15 ' , ' 16 ' , ' 17 ' , ' 18 ' , ' 19 ' , ' 20 ' , ' 21 ' , ' 22 ' , ' 23 ' , ' 24 ' , ' 25 ' , ' 26 ' , ' 27 ' , ' 28 ' , ' 29 ' , ' 30 ' , ' 31 ' , ' 32 ' , ' 33 ' , ' 34 ' , ' 35 ' , ' 36 ' , ' 37 ' , ' 38 ' , ' 39 ' , ' 40 ' , ' 41 ' , ' 42 ' , ' 43 ' , ' 44 ' , ' 45 ' , ' 46 ' , ' 47 ' , ' 48 ' , ' 49 ' , ' 50 ' , ' 51 ' , ' 52 ' , ' 53 ' , ' 54 ' , ' 55 ' , ' 56 ' , ' 57 ' , ' 58 ' , ' 59 ' , '60']
            string1a60 = [' 0 ' , ' 1 ' , ' 2 ' , ' 3 ' , ' 4 ' , ' 5 ' , ' 6 ' , ' 7 ' , ' 8 ' , ' 9 ' , ' 10 ' , ' 11 ' , ' 12 ' , ' 13 ' , ' 14 ' , ' 15 ' , ' 16 ' , ' 17 ' , ' 18 ' , ' 19 ' , ' 20 ' , ' 21 ' , ' 22 ' , ' 23 ' , ' 24 ' , ' 25 ' , ' 26 ' , ' 27 ' , ' 28 ' , ' 29 ' , ' 30 ' , ' 31 ' , ' 32 ' , ' 33 ' , ' 34 ' , ' 35 ' , ' 36 ' , ' 37 ' , ' 38 ' , ' 39 ' , ' 40 ' , ' 41 ' , ' 42 ' , ' 43 ' , ' 44 ' , ' 45 ' , ' 46 ' , ' 47 ' , ' 48 ' , ' 49 ' , ' 50 ' , ' 51 ' , ' 52 ' , ' 53 ' , ' 54 ' , ' 55 ' , ' 56 ' , ' 57 ' , ' 58 ' , ' 59 ' , '60']
            bg = tk.PhotoImage(file='images/BGconfig1.png')
            frameBG = ctk.CTkFrame(settingswindow,300,300)
            frameBG.place(x=0,y=0)
            labelBG = ctk.CTkLabel(frameBG,300,300,text=' ',image=bg)
            labelBG.place(x=0,y=0)
            minuteSelection = ctk.CTkComboBox(frameBG,85,30,values=string0a60,
                                              dropdown_fg_color='#6f6f6f',fg_color='#6f6f6f',
                                              font=('Minecraft', fontsize), command=callback_Study_min)
            minuteSelection.place(x=60,y=60)
            secondsSelection = ctk.CTkComboBox(frameBG,85,30,values=string0a60,
                                               dropdown_fg_color='#6f6f6f',fg_color='#6f6f6f',
                                               font=('Minecraft', fontsize), command=callback_Study_sec)
            secondsSelection.place(x=150,y=60)
            studylabel = tk.PhotoImage(file='images/StudySettings.png', width=146,height=38)
            minutesSelectionLabel = ctk.CTkLabel(frameBG,image=studylabel,text=' ')
            minutesSelectionLabel.place(x=75,y=10)
            relaxlabel = tk.PhotoImage(file='images/RelaxSetting.png', width=139,height=38)
            relaxSelectionLabel = ctk.CTkLabel(frameBG,image=relaxlabel,text=' ')
            relaxSelectionLabel.place(x=75,y=125)
            relaxminuteSelection = ctk.CTkComboBox(frameBG,85,30,values=string1a60,
                                                   dropdown_fg_color='#6f6f6f',
                                                   fg_color='#6f6f6f',
                                                   font=('Minecraft', fontsize), command=callback_relax_min)
            relaxminuteSelection.place(x=60,y=180)
            relaxsecondsSelection = ctk.CTkComboBox(frameBG,85,30,values=string1a60,
                                                    dropdown_fg_color='#6f6f6f',
                                                    fg_color='#6f6f6f',
                                                    font=('Minecraft', fontsize), command=callback_relax_sec)
            relaxsecondsSelection.place(x=150,y=180)

            submit = ActionButtons(frameBG,text="submit", command= lambda: submitgo())
            submit.place(x=75,y=230)



        # #* Variaveis globais de Tempo
        # global minStudy
        # global secStudy
        # global secRelax
        # global minRelax
        # secStudy = 0
        # minStudy = 5
        # secRelax = 0
        # minRelax = 3

        # #* Variaveis globais de Flag
        # global reset
        # global runningStudy
        # global runningRelax
        # global pauseRelax
        # global pauseStudy
        # reset = False
        # runningStudy = False
        # runningRelax = False
        # pauseRelax = False
        # pauseStudy = False

        def start():
            global minStudy
            global secStudy
            global secRelax
            global minRelax

            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy

            if (not(runningStudy) and not(pauseStudy)) and (not(runningRelax) and not(pauseRelax)):
                runningStudy =True
                startPause.configure(text="pause", command= lambda: pause())
                return attStudy(minStudy, secStudy)
            
            if runningStudy or pauseStudy:
                runningStudy=True
                pauseStudy = False
                startPause.configure(text="pause", command= lambda: pause())
                return attStudy(int(minLabel._text),int(secLabel._text))
            
            if runningRelax or pauseRelax:
                runningRelax = True
                pauseRelax = False
                startPause.configure(text="pause", command= lambda: pause())
                return attRelax(int(minLabel._text),int(secLabel._text))            

        def pause():
            global minStudy
            global secStudy
            global secRelax
            global minRelax

            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            if runningStudy:
                runningStudy = False
                pauseStudy = True

            if runningRelax:
                runningRelax = False
                pauseRelax = True
            
            startPause.configure(text='continue', command=lambda:start())

        def restart():
            global minStudy
            global secStudy
            global secRelax
            global minRelax

            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            
            if runningStudy or pauseStudy:
                runningStudy=False
                pauseStudy = True
                startPause.configure(text="continue", command= lambda: start())
                secLabel.configure(text=TimeTransform().transform(secStudy))
                minLabel.configure(text=TimeTransform().transform(minStudy))
                return 
            
            if runningRelax or pauseRelax:
                runningRelax = False
                pauseRelax = True
                startPause.configure(text="continue", command= lambda: start())
                secLabel.configure(text=TimeTransform().transform(secRelax))
                minLabel.configure(text=TimeTransform().transform(minRelax))
                return           

        def skip():
            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            print('runningStudy',runningStudy,'runningRelax',runningRelax, 'pauseRelax',pauseRelax, 'pauseStudy', pauseStudy)

            if runningStudy or pauseStudy:
                pauseStudy = False
                runningStudy = False
                pauseRelax = True
                startPause.configure(text='continue', command=lambda:start())
                return studyRelax()
            if runningRelax or pauseRelax:
                pauseRelax = False
                runningRelax = False
                pauseStudy = True
                startPause.configure(text='continue', command=lambda:start())
                return studyRelax()

        def attStudy(minRunning = int(minLabel._text), secRunning = int(secLabel._text)):
            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy

            print(int(minLabel._text),int(secLabel._text))
            if runningStudy:
                if not(secRunning):
                    minRunning = minRunning - 1
                    minRunning = minRunning%60
                secRunning = secRunning - 1
                secRunning = secRunning%60
                secLabel.configure(text=TimeTransform().transform(secRunning))
                minLabel.configure(text=TimeTransform().transform(minRunning))
                self.after(1000, lambda: attStudy(int(minLabel._text),int(secLabel._text)))
            if secRunning < 1 and minRunning < 1:
                runningStudy = False
                pauseRelax = True
                startPause.configure(text='continue', command=lambda:start())
                return studyRelax()
                
        def attRelax(minRunning = (int(minLabel._text)), secRunning = int(secLabel._text)):
            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy

            print(int(minLabel._text),int(secLabel._text))
            if runningRelax:
                if not(secRunning):
                    minRunning = minRunning - 1
                    minRunning = minRunning%60
                secRunning = secRunning - 1
                secRunning = secRunning%60
                secLabel.configure(text=TimeTransform().transform(secRunning))
                minLabel.configure(text=TimeTransform().transform(minRunning))
                self.after(1000, lambda: attRelax(minRunning,secRunning ))
            if secRunning < 1 and minRunning < 1:
                runningRelax = False
                pauseStudy = True
                startPause.configure(text='continue', command=lambda:start())
                return studyRelax()

        def studyRelax():
            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            global minStudy
            global secStudy
            global secRelax
            global minRelax

            if pauseRelax:
                secLabel.configure(text=TimeTransform().transform(secRelax))
                minLabel.configure(text=TimeTransform().transform(minRelax))

            if pauseStudy:
                secLabel.configure(text=TimeTransform().transform(secStudy))
                minLabel.configure(text=TimeTransform().transform(minStudy))



        























'''       
        def start():
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            # print('runningStudy',runningStudy,'runningRelax',runningRelax, 'pauseRelax',pauseRelax, 'pauseStudy', pauseStudy)

            if (runningRelax == pauseRelax) == (runningStudy == pauseStudy):
                runningStudy = True
                startPause.configure(text='pause', command=lambda:pause())
                return att(int(secLabel._text),int(minLabel._text))
            
            if pauseRelax:
                pauseRelax = False
                runningRelax = True
                startPause.configure(text='pause', command=lambda:pause())
                return att2(int(secLabel._text), int(minLabel._text))
            if pauseStudy:
                pauseStudy = False
                runningStudy = True
                startPause.configure(text='pause', command=lambda:pause())
                
                
                return att(int(secLabel._text),int(minLabel._text) )

            # runningStudy = True
            # startPause.configure(text="pause", command= lambda: pause())
            # study()
        
        def skip():
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            
            global min
            global secRelax
            global sec
            global minRelax
            print('runningStudy',runningStudy,  'pauseStudy',pauseStudy, 'runningRelax',  runningRelax, 'pauseRelax',pauseRelax )

            if runningStudy or pauseStudy:
                pause2()
                runningStudy = False
                pauseStudy = False
                pauseRelax = True
                return att2(secRelax +2, minRelax)
            
            
            if runningRelax or pauseRelax:
                pause2()
                runningStudy = True
                runningRelax = False
                pauseRelax = False
                return att(sec +2, min)
            
            pauseRelax = True
            return att2(secRelax, minRelax)
            
        def att(sec = int(secLabel._text), min = int(minLabel._text)):
            # print(min, sec)
            global secRelax
            global minRelax
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            global reset

            if runningStudy:    
                if not(sec):
                    min = min - 1
                    min = min%60
                sec = sec - 1
                sec = sec%60
                # print(min, sec)
                secLabel.configure(text=TimeTransform().transform(sec))
                minLabel.configure(text=TimeTransform().transform(min))
                self.after(1000, lambda: att(sec, min))
                if sec < 1 and min < 1:
                    secLabel.configure(text=TimeTransform().transform(sec))
                    minLabel.configure(text=TimeTransform().transform(min))
                    runningStudy = False
                    pauseRelax = True
                    startPause.configure(text='continue', command=lambda:start())
                    return
            else:
                secLabel.configure(text=TimeTransform().transform(sec))
                minLabel.configure(text=TimeTransform().transform(min))
                if reset:
                    reset = False
                    resete()
                return
            # secLabel.configure(text=TimeTransform().transform(sec))
            # minLabel.configure(text=TimeTransform().transform(min))

        def att2(sec = int(secLabel._text), min = int(minLabel._text)):

            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            global reset
            if runningRelax:    
                print('Rodando relax', runningRelax)
                if not(sec):
                    min = min - 1
                    min = min%60
                sec = sec - 1
                sec = sec%60
                print(min, sec)
                secLabel.configure(text=TimeTransform().transform(sec))
                minLabel.configure(text=TimeTransform().transform(min))
                self.after(1000, lambda: att2(sec, min))
                if sec < 1 and min < 1:
                    secLabel.configure(text=TimeTransform().transform(sec))
                    minLabel.configure(text=TimeTransform().transform(min))
                    runningRelax = False
                    pauseStudy = True
                    startPause.configure(text='continue', command=lambda:start())
                    return
            else:
                secLabel.configure(text=TimeTransform().transform(sec))
                minLabel.configure(text=TimeTransform().transform(min))
            if reset:
                reset = False
                resete()
                return
            secLabel.configure(text=TimeTransform().transform(sec))
            minLabel.configure(text=TimeTransform().transform(min))

        def pause2():
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            if runningStudy:
                runningStudy = False
            if runningRelax:
                runningRelax = False
            startPause.configure(text='pause', command=lambda:pause())

        def pause():
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy

            if runningStudy:
                runningStudy = False
                pauseStudy = True

            if runningRelax:
                runningRelax = False
                pauseRelax = True
            startPause.configure(text='continue', command=lambda:start())
            
        def resetar():
            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            
            global min
            global secRelax
            global sec
            global minRelax
            
            reset = True
            pause()
            return

        def resete():
            global reset
            global runningStudy
            global runningRelax
            global pauseRelax
            global pauseStudy
            global min
            global secRelax
            global sec
            global minRelax

            if runningStudy or pauseStudy:
                print('passou')
                print(min,sec)
                secLabel.configure(text=TimeTransform().transform(sec))
                minLabel.configure(text=TimeTransform().transform(min))
            if runningRelax or pauseRelax:
                secLabel.configure(text=TimeTransform().transform(secRelax))
                minLabel.configure(text=TimeTransform().transform(minRelax))

'''