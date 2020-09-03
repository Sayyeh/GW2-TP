from GW2TP import GW2Alarm
from GW2TPUI import GW2GUI

class Controller:

    def __init__(self):
        self.tp = GW2Alarm(self)
        self.gui = GW2GUI(self)

    def getController(self):
        return self

    def getTP(self):
        return self.tp

    def getGUI(self):
        return self.gui

    def cConvertCtoG(self, pCoin: int):
        self.tp.ConvertCtoGSC(pCoin)

    def cConvertGtoC(self, pGold: int, pSilber: int, pBronze: int):
        self.tp.ConvertGSCtoC(pGold, pSilber, pBronze)

    def cSetAPI(self, pAPI):
        self.tp.setAPI(pAPI)

a = Controller()
a.getGUI().main.mainloop()