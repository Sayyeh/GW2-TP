from gw2api import GuildWars2Client
from win10toast import ToastNotifier
import json

# print(client.commercedelivery.get())
# print(client.accountinventory.get())
#accountinventory|accountwallet|commercedelivery|commerce/transactions|commerce/prices|commerce/listings

class GW2Alarm:
    #"E266A2C1-5D3F-124F-A518-340D555309A77F9EEF41-3882-4964-A367-867C698225A6" Test API
    def __init__(self, pContoller: object = None, pAPI: str = None):
        self.API = pAPI
        self.controller = pContoller
        self.toast = ToastNotifier() #Win10 Notification
        self.client = GuildWars2Client(api_key = self.API)  # Mit der GW2 API verbinden
        self.itemL = {}
        self.itemID = {}
        self.noti = ToastNotifier()

    def setAPI(self, pAPI:str):
        self.API = pAPI

    def getItemL(self): #Return Liste mit allen überwachten Items
        return self.itemL

    def getItemLID(self):
        return self.itemID

    def setItemL(self, pItem: str, pCoin: int): #Füge Item der Überwachungsliste hinzu oder verändere es
        self.itemL[pItem] = pCoin
        self.itemID[pItem] = self.getId(pItem)

    @staticmethod
    def ConvertCtoGSC(pCoin: int): #Umwandeln von Coins in Gold, SIlber Bronze
        Gold = pCoin / 10000

        if len(str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1]) == 1:
            Silber = str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1] + "0"
        else:
            Silber = str(Gold)[len(str(pCoin)) - 3:len(str(pCoin)) - 1]

        if len(str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1]) == 1:
            Bronze = str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1] + "0"
        elif str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1] == "":
            Bronze = "0"
        else:
            Bronze = str(Gold)[len(str(pCoin)) - 1:len(str(pCoin)) + 1]

        #print(Gold, Silber, Bronze)

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

        bPreis = self.client.commerceprices.get(id = self.getId(pItem))

        return bPreis[pVersion]["unit_price"]

    def getClient(self):
        return self.client

    def getDelivery(self):
        return self.client.commercedelivery.get()

    def winNoti(self, pItem, pPreis):
        commerce = self.ConvertCtoGSC(int(pPreis))
        self.noti.show_toast("GW2 Price Alarm", "Item {} hat Preis {} Gold {} Silber {} Copper erreicht".format(pItem, commerce[0], commerce[1], commerce[2]),
                             duration=20, icon_path = "images\icon.ico", threaded = True)

if __name__ == "__main__":
    a = GW2Alarm("E266A2C1-5D3F-124F-A518-340D555309A77F9EEF41-3882-4964-A367-867C698225A6")
    print(a.getId("Mystic Coin"))
    #print(a.getClient().commerceprices.get(id=a.getId("Silk Patch")))
    #print(a.ConvertCtoGSC(a.getClient().commerceprices.get(id=a.getId("Silk Patch"))["buys"]["unit_price"]))
    a.setItemL("Mystic Coin", 1)
    a.setItemL("Elonian Greatblade", 1)
    a.setItemL("+1 Agony Infusion", 1)
    a.setItemL("+15 Agony Infusion", 1)

    print(a.getItemLID())
    b = a.client.commerceprices.get(id = a.getId("Mystic Coin"))