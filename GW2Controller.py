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
        return self.tp.ConvertCtoGSC(pCoin)

    def cConvertGtoC(self, pGold: int, pSilber: int, pBronze: int):
        return self.tp.ConvertGSCtoC(pGold, pSilber, pBronze)

    def cSetAPI(self, pAPI):
        return self.tp.setAPI(pAPI)

    def cGetPreise(self, pItem: str, pVersion: str):
        pVersion = pVersion.lower() + "s"
        return self.tp.getPreis(pItem, pVersion)

a = Controller()
a.getGUI().main.mainloop()