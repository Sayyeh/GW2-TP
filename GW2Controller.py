from GW2TP import GW2Alarm
from GW2TPUI import GW2GUI

class Controller:
    #COntroller dient als Schnittstelle zwischen GUI und Rest
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

    def cSetAPI(self, pAPI: str):
        return self.tp.setAPI(pAPI)

    def cGetPreise(self, pItem: str, pVersion: str):
        pVersion = pVersion.lower() + "s"
        return self.tp.getPreis(pItem, pVersion)

    def cSetItemL(self, pItem, pPreis, pVersion, pOperator, pAnzahl):
        self.tp.setItemL(pItem, pPreis, pVersion, pOperator, pAnzahl)

    def cRemoveItemL(self, pItem: str):
        self.tp.removeItemL(pItem)

    def cGetID(self, pItem: str):
        return self.tp.getId(pItem)

    def cSaveItem(self):
        self.tp.saveData()

    def cReadItem(self):
        return self.tp.readData()

    def cNoti(self, pItem: str, pPreis: int, pVersion: str, pOperator: str):
        self.tp.winNoti(pItem, pPreis, pVersion, pOperator)

    def cSetDelay(self, pDelay: int):
        self.tp.setDelay(pDelay)

    def cGetItem(self, pItem: str):
        return self.tp.getItem(pItem)

#a = Controller()
#a.getGUI().main.mainloop()