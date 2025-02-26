import time, threading

defaultSimbol = "✆ "
lineSimbol = "█ "
arrowSimbol = "▼ "
borderSimbol = " ▞ "
lineLowSimbol = "━ "

lvls = [[11, 5, 0.5], # 1 - Размер по x [ рекомендуется не чётное ], 2 - размер по y, 3 - таймер обновления
        [13, 7, 0.4],
        [9, 9, 0.3],
        [7, 11, 0.25],
        [7, 6, 0.5, [9, 3]],
        [9, 8, 0.35, [2, 5]]
        ]

secondary_middles = []

class QuadroGame:
    def __init__(self):
        self.current_lvl = 5
        self.x = lvls[self.current_lvl][1]
        self.y = lvls[self.current_lvl][0]
        self.time = lvls[self.current_lvl][2]
        self.quads = [[defaultSimbol]* self.x for i in range(self.y)]
        if len(lvls[self.current_lvl])>=3:
            for i in range(3, len(lvls[self.current_lvl])):
                secondary_middles.append(lvls[self.current_lvl][i])
                self.y+=1
            #print(secondary_middles)
        self.gameEnd = False
        self.curX = 0
        self.curY = 0
        self.curMiddle = 0
        self.curNumMiddle = 0
        self.check = False
        self.died = False
        
    def setUp(self):
        self.x = lvls[self.current_lvl][1]
        self.y = lvls[self.current_lvl][0]
        self.time = lvls[self.current_lvl][2]
        self.quads = [[defaultSimbol]* self.x for i in range(self.y)]
        secondary_middles=[]
        if len(lvls[self.current_lvl])>=3:
            for i in range(3, len(lvls[self.current_lvl])):
                secondary_middles.append(lvls[self.current_lvl][i])
                self.x+=1
                #for i in range(cru)
                self.quads[secondary_middles[i-3][0]][secondary_middles[i-3][1]-1] = lineSimbol
            #print(secondary_middles)
        self.gameEnd=False
        self.curX=0
        self.curY=0
        self.curMiddle=0
        self.curNumMiddle = 0
        self.check = False
        self.died = False
        self.startQuad()
        
    def gameResult(self, result):
        if result==True:
            print("◄ "+str(" ▰"*int(mainGame.y+1)))
            print("   ЦЕНТР ВЗЯТ ☻  ")
            print("◄ "+str(" ▰"*int(mainGame.y+1)))
            if self.current_lvl>=len(lvls):
                self.current_lvl=0
            else:
                self.current_lvl+=1
            time.sleep(1)
        else:
            print("◄ "+str(" ▰"*int(mainGame.y+1)))
            print(" ИГРА ПРОИГРАНА ☢ ")
            print("◄ "+str(" ▰"*int(mainGame.y+1)))
            time.sleep(1)
        
    def setQuad(self, x0, y0):
            
        if (self.diedCheck()==True):
            self.died=True    
        self.quads[x0][y0] = lineSimbol
        try:
            self.quads[self.curX-1][self.curY] = defaultSimbol
        except ValueError:
            pass
        
        self.curX=0
        self.curY+=1
        if self.curNumMiddle < len(secondary_middles) and self.curY == secondary_middles[self.curNumMiddle][1]:
            print("NGNJWEGJKENWJKGW "+str(secondary_middles[self.curNumMiddle][0]))
            self.curMiddle=secondary_middles[self.curNumMiddle][0]
            self.curNumMiddle+=1
        
    def moveQuad(self):
        if self.curY <= self.x-2:
            try:
                if self.quads[self.curX][self.curY]!=lineSimbol:
                    self.quads[self.curX][self.curY] = arrowSimbol
            except ValueError:
                pass
            
            try:
                if self.quads[self.curX-1][self.curY]!=lineSimbol:
                    self.quads[self.curX-1][self.curY] = defaultSimbol
            except ValueError:
                pass
            self.curX+=1
        
        
    def startQuad(self):
        self.curMiddle = self.y//2
        self.setQuad(self.curMiddle, 0)
        
    def printQuad(self):
        if self.curY<=self.x:
            quadStr=""
            for i in range(self.x-1):
                for j in range(self.y):
                    quadStr+=self.quads[j][i]

                if i+1<10:
                    print("0"+str(i+1)+borderSimbol+quadStr)
                else:
                    print(str(i+1)+borderSimbol+quadStr)
                quadStr=""
            
    def diedCheck(self, check0=None):
        if check0==True:
            self.check=check0
        #print(self.check)
        
        if self.curX>self.curMiddle:
            self.curNumMiddle=0
            secondary_middles = []
            return True
        elif self.curX<self.curMiddle and self.check==True:
            self.curNumMiddle=0
            secondary_middles = []
            return True
        else:
            return False

choose = input("Хотите ли вы узнать правила игры? [Y/N] \nВаш Ответ: ")

if str(choose).lower()=="y":
    print("◤ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
    print("   Правила игры\n")
    print("Используйте ENTER, чтобы поставить стрелочку\nНажимайте клавишу заранее на 1 клетку до центральной линии\nВсего в игре "+str(len(lvls))+" уровней\n")
    print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
    choose = input("Вы хотите начать играть? [Нажмите ENTER]")

mainGame = QuadroGame()
    
def gameLoop():
    while(True):
        if mainGame.current_lvl>=len(lvls):
            print("\n◤ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
            print("   ИГРА УСПЕШНО ПРОЙДЕНА  \n")
            print("   УРОВНИ ПОЙДУТ СНАЧАЛА  ")
            print("◣ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰ ▰\n")
            mainGame.current_lvl=0
            time.sleep(1)
        #print("◤ Длина по оси Х: "+str(lvls[mainGame.current_lvl][0])
        #      +"\n┃ Длина по оси Y: "+str(lvls[mainGame.current_lvl][1])
        #      +"\n◣ Частота обновления: "+str(lvls[mainGame.current_lvl][2])+"\n")
        mainGame.gameEnd=False
        if mainGame.gameEnd==False:
            mainGame.setUp()
            #mainGame.printQuad()
            while(mainGame.gameEnd==False):
                if mainGame.diedCheck()==True or mainGame.died==True: #проигрыш
                    mainGame.gameEnd==True
                    mainGame.gameResult(False)
                    break
                
                if mainGame.curY == mainGame.x-1: # победа
                    mainGame.gameEnd==True
                    mainGame.gameResult(True)
                    break
                
                time.sleep(mainGame.time)
                mainGame.check=False
                mainGame.moveQuad()
                print("У-"+str(mainGame.current_lvl)+str(" ▰"*int(mainGame.y+1)))
                mainGame.printQuad()
                #print("curY = "+str(mainGame.curY)+"; Y = "+str(mainGame.x-1)+"; NEW MIDDLE = "+str(mainGame.curMiddle))
                    
def checkEnter():
    while(mainGame.gameEnd==False):
        enterKey = None
        enterKey = input("")
        if enterKey != None:
            mainGame.diedCheck(True)
            mainGame.setQuad(mainGame.curX, mainGame.curY)
            
gameThread = threading.Thread(target=gameLoop)
checkThread = threading.Thread(target=checkEnter)

gameThread.start()
checkThread.start()

gameThread.join()
checkThread.join()
