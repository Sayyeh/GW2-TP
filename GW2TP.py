from GW2TPAPI import GW2API
from win10toast import ToastNotifier
from GW2Json import GW2Json
from GW2Item import GW2Item
import json

class GW2Alarm:
    #"E266A2C1-5D3F-124F-A518-340D555309A77F9EEF41-3882-4964-A367-867C698225A6" Test API
    def __init__(self, pContoller: object = None, pAPI: str = None):
        self.API = pAPI
        self.controller = pContoller
        self.toast = ToastNotifier() #Win10 Notification
        self.client = GW2API(pAPI = self.API)  # Mit der GW2 API verbinden
        self.itemL = {}
        self.noti = ToastNotifier()
        self.data = GW2Json()
        self.delay = 20

    def readData(self): #Lese Items vom Speicher
        return self.data.jsonRead()

    def saveData(self): #Schreibe Items in den Speicher
        self.data.jsonCreate(self.itemL)

    def setAPI(self, pAPI: str): #Setze den API-Key
        self.client.setAPI(pAPI)

    def getItem(self, pItem): #Return Item
        return self.itemL[pItem]

    def setItemL(self, pItem: str, pPreis, pVersion, pOperator, pAnzahl): #Füge Item der Überwachungsliste hinzu oder verändere es
        self.itemL[pItem] = GW2Item(pItem, pPreis, pVersion, pOperator, pAnzahl)   #self.getId(pItem)
        self.itemL[pItem].setId(self.getId(pItem))

    def removeItemL(self, pItem: str): #Lösche Item aus der Liste
        del self.itemL[pItem]
        self.itemL.pop(pItem, None)

    @staticmethod
    def ConvertCtoGSC(pCoin: int): #Umwandeln von Coins in Gold, Silber Bronze (Nicht die beste und effizienteste Variante, aber psscht)
        Gold = pCoin / 10000

        if len(str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1]) == 1 and len(str(pCoin)) > 4:
            Silber = str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1] + "0"
        elif len(str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1]) > 1 and len(str(pCoin)) > 4:
            Silber = str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1]
        else:
            Silber = str(pCoin)[0:len(str(pCoin)) - 2]

        if len(str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1]) == 1 and len(str(pCoin)) > 4:
            Bronze = str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1] + "0"
        elif len(str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1]) > 1 and len(str(pCoin)) > 4:
            Bronze = str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1]
        elif not str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1] or not str(Gold)[2:len(str(pCoin))]:
            Bronze = "0"
        else:
            Bronze = str(pCoin)[len(str(pCoin)) - 2:len(str(pCoin))]

        if len(str(pCoin)) <= 2:
            Gold = "0"
            Silber = "0"
            Bronze = pCoin

        return int(float(Gold)), int(float(Silber)), int(float(Bronze))

    @staticmethod
    def ConvertGSCtoC(pGold: int, pSilber: int, pBronze: int): #Umwandeln von Gold, SIlber Bronze in Coins
        Gold = str(pGold)

        if pSilber < 10:
            Silber = "0" + str(pSilber)
        else:
            Silber = str(pSilber)

        if pBronze < 10:
            Bronze = "0" + str(pBronze)
        else:
            Bronze = str(pBronze)

        return int(Gold + Silber + Bronze)

    @staticmethod
    def getId(pName: str): #Item-Id anhand des Namens ermitteln
        Path = "Json/gw2Datasheet.json"
        itemID = None

        with open(Path, "r+") as fi: #Json FIle öffnen
            f = json.load(fi)

        for i in range(len(f)): #Json file durchsuchen nach Item
            if f[i]["name"] == pName:
                itemID = f[i]["data_id"]

        return itemID

    def getPreis(self, pItem: str, pVersion: str):
        # Hole buy und sell Preise der überwachten Items

        bPreis = self.client.getCommerceprices(pId=self.itemL[pItem].getId())

        return bPreis[pVersion]["unit_price"]

    def getClient(self): #Return self
        return self.client

    # def getDelivery(self): #Noch nicht von nutzen
    #     return self.client.commercedelivery.get()

    def winNoti(self, pItem: str, pPreis: int, pVersion: str, pOperator: str): #Win10 Benachrichtigung mit extra Infos
        commerce = self.ConvertCtoGSC(pPreis)
        operator = "über" if pOperator == "Größer" else "unter"
        self.noti.show_toast("GW2 Price Alarm", "Item {} ist {} Preis {} Gold {} Silber {} Copper \n{} Order".format(pItem, operator, commerce[0], commerce[1], commerce[2], pVersion),
                             duration=self.delay, icon_path = "images\icon.ico", threaded = True)

    def setDelay(self, pDelay: int):
        self.delay = pDelay

if __name__ == "__main__": #Zum Testen
    a = GW2Alarm()
    print(a.getId("Mystic Coin"))
    print(a.getPreis("19976", "buys"))

