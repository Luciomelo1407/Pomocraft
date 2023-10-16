# por enquanto será apenas um teste para a classe de tempo

import time
class Timer:
    def __init__(self, secRunning, minRunning, hour) -> None:
        self.secRunning = secRunning
        self.minRunning = minRunning
        self.hour = hour

    def play(self):
        while self.secRunning > 0 or self.hour > 0 or self.minRunning > 0:
            print(self.hour,":",self.minRunning,":",self.secRunning)
            if not(self.minRunning) and self.hour > 0:
                self.hour = self.hour -1
            if not(self.secRunning):
                self.minRunning = self.minRunning - 1
                self.minRunning = self.minRunning%60
            self.secRunning = self.secRunning - 1
            self.secRunning = self.secRunning%60
            time.sleep(1)
        print(self.hour,":",self.minRunning,":",self.secRunning)    

    def getSecRunning(self):
        return self.secRunning

    def getMinRunning(self):
        return self.minRunning
    
    def getHour(self):
        return self.hour



seila = Timer(0,1,0)
seila.play()




'''        
secRunning = 0
minRunning = 0
hour = 1


while secRunning > 0 or hour > 0 or minRunning > 0:
    print(hour,":",minRunning,":",secRunning)
    if not(minRunning) and hour > 0:
        hour = hour -1
    if not(secRunning):
        minRunning = minRunning - 1
        minRunning = minRunning%60
    secRunning = secRunning - 1
    secRunning = secRunning%60
    time.sleep(0.0001)
print(hour,":",minRunning,":",secRunning)

'''
