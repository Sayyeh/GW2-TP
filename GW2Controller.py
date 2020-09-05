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

    def cSetItemL(self, pItem: str):
        self.tp.setItemL(pItem)

    def cRemoveItemL(self, pItem: str):
        self.tp.removeItemL(pItem)

    def cGetItemP(self):
        return self.gui.getItemLP()

    def cGetItemV(self):
        return self.gui.getItemLV()

    def cSaveItem(self, pItemP, pItemV):
        self.tp.saveData(pItemP, pItemV)

    def cReadItem(self):
        return self.tp.readData()

    def cNoti(self, pItem, pPreis):
        self.tp.winNoti(pItem, pPreis)

a = Controller()
a.getGUI().main.mainloop()