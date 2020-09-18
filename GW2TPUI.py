import tkinter as tk
from tkinter import ttk

class GW2GUI:

    def __init__(self, pController):
        self.main = tk.Tk()
        self.main.title("Gw2 Alarm")
        self.main.geometry("495x495+0+0")
        self.main.resizable(False, False)
        self.main.configure(background="#383a39")
        self.main.iconbitmap("Images/icon.ico")
        self.controller = pController
        self.itemUIP = {}
        self.itemUIV = {}
        self.itemUIG = {}
        self.widgets = []
        self.imgGold = tk.PhotoImage(file = "Images/Gold_coin.png")
        self.imgSilber = tk.PhotoImage(file = "Images/Silver_coin.png")
        self.imgBronze = tk.PhotoImage(file = "Images/Copper_coin.png")
        self.v = tk.IntVar()
        self.g = tk.IntVar()
        self.b = tk.StringVar()
        self.u = tk.StringVar()

        self.title = tk.Label(self.main, text = "GW2 Price Alarm", font = ("Verdanan", 21, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                             activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0)
        self.title.place(x = 0, y = 0)

        self.ladenButton = tk.Button(self.main, text = "Laden", font = ("Verdanan", 11, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                     activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "normal",
                                     disabledforeground= "#494a49", command = self.startGUI)
        self.ladenButton.place(x = 0, y = 35)

        self.tpItem = tk.Listbox(self.main, bg = "#1c1d1c", font = ("Verdanan", 10, "bold"), bd = 0, highlightthickness = 0, selectbackground = "#ce480f", fg = "white")
        self.tpItem.place(x = 0, y = 60)

        self.tpButton = tk.Button(self.main, text = "Item hinzufügen", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "disabled",
                                   disabledforeground= "#494a49", command = self.addItem)
        self.tpButton.place(x = 140, y = 60)

        self.tpRemove = tk.Button(self.main, text = "Item löschen", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "disabled",
                                   disabledforeground= "#494a49", command = self.removeItem)
        self.tpRemove.place(x = 353, y = 60)


        self.tpEntry = tk.Entry(self.main, bg = "#1c1d1c", fg = "#EEE9E9", width = 50, bd = 0, state = "disabled", disabledbackground = "#494a49", disabledforeground= "#EEE9E9")
        self.tpEntry.place(x = 140, y = 85)

        self.goldEntry = tk.Entry(self.main, bg="#1c1d1c", fg="#EEE9E9", width=4, bd=0, state="disabled", disabledbackground="#494a49", disabledforeground="#EEE9E9")
        self.goldEntry.place(x = 140, y = 102)

        self.goldT = tk.Label(self.main, image = self.imgGold, bg = "#383a39")
        self.goldT.place(x = 167, y = 102)

        self.silberEntry = tk.Entry(self.main, bg="#1c1d1c", fg="#EEE9E9", width=4, bd=0, state="disabled", disabledbackground="#494a49", disabledforeground="#EEE9E9")
        self.silberEntry.place(x = 190, y = 102)

        self.silberT = tk.Label(self.main, image = self.imgSilber, bg = "#383a39")
        self.silberT.place(x = 217, y = 102)

        self.bronzeEntry = tk.Entry(self.main, bg="#1c1d1c", fg="#EEE9E9", width=4, bd=0, state="disabled", disabledbackground="#494a49", disabledforeground="#EEE9E9")
        self.bronzeEntry.place(x = 240, y = 102)

        self.bronzeT = tk.Label(self.main, image = self.imgBronze, bg = "#383a39")
        self.bronzeT.place(x = 267, y = 102)

        self.buyRadio = tk.Radiobutton(self.main, text = "Buy order", variable = self.v, value = 1, bg = "#383a39", fg = "#EEE9E9",
                                       activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "disabled")
        self.buyRadio.place(x = 140, y = 120)

        self.sellRadio = tk.Radiobutton(self.main, text = "Sell order", variable = self.v, value = 2, bg = "#383a39", fg = "#EEE9E9",
                                       activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "disabled")
        self.sellRadio.place(x = 140, y = 138)

        self.boxInfo = tk.Label(self.main, textvariable = self.b, font = ("Verdanan", 10, "bold"), bg="#383a39", fg="#EEE9E9")
        self.boxInfo.place(x =  140, y = 166)

        self.updateOption = ttk.Combobox(self.main, textvariable = self.u, state = "disabled")
        self.updateOption.place(x = 0, y = 233)
        self.updateOption.bind("<Key>", lambda e: "break")

        self.updateLabel = tk.Label(self.main, text = "Wie oft soll geupdated \nwerden?", font = ("Verdanan", 9, "bold"), bg="#383a39", fg="#EEE9E9")
        self.updateLabel.place(x = 0, y = 255)

        self.saveButton = tk.Button(self.main, text = "Speichern", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "disabled",
                                   disabledforeground= "#494a49", command = self.saveItem)
        self.saveButton.place(x = 368, y = 104)

        self.biggerRadio = tk.Radiobutton(self.main, text = "TP Preis größer", variable = self.g, value = 1, bg = "#383a39", fg = "#EEE9E9",
                                       activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "disabled")
        self.biggerRadio.place(x = 220, y = 120)

        self.smallerRadio = tk.Radiobutton(self.main, text = "TP Preis kleiner", variable = self.g, value = 2, bg = "#383a39", fg = "#EEE9E9",
                                       activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "disabled")
        self.smallerRadio.place(x = 220, y = 138)

        self.priceUpdate(0)

    def readItem(self, pIndex = 0): #Lese Items aus dem Speicher
        temp = self.controller.cReadItem()

        if temp[0] and pIndex + 1 <= len(temp[0]): #Items werden der Reihe nach geladen
            i = list(temp[0])[pIndex]
            self.addDataItem(i, temp[0][i], temp[1][i], temp[2][i])

            self.main.after(10, self.readItem, pIndex + 1)

    def saveItem(self): #Speichere Items in den Spreicher
        self.controller.cSaveItem(self.itemUIP, self.itemUIV, self.itemUIG)

    def startGUI(self): #GUI starten und entsperren (war früher startAPI())
        if self.tpButton["state"] == "disabled":
            self.widgets = [self.tpItem, self.tpButton, self.tpEntry, self.goldEntry, self.goldT,
                            self.silberEntry, self.silberT, self.bronzeEntry, self.bronzeT, self.buyRadio,
                            self.sellRadio, self.tpRemove, self.updateOption, self.saveButton, self.biggerRadio,
                            self.smallerRadio]  # Alle Widgets

            for i in self.widgets:  # Widgets werden entsperrt
                i.config(state="normal")
            self.v.set(1)
            self.g.set(1)
            self.updateOption["values"] = ["1 min", "2 min", "3 min", "4 min", "5 min"]
            self.u.set("2 min")
            self.boxUpdate()
        if len(self.itemUIP) == 0:  # Wenn was im Speicher, lade ihn
            self.readItem()

    def removeItem(self): #Item aus der Listbox entfernen
        if self.tpItem.curselection():
            item = self.tpItem.get(self.tpItem.curselection())
            self.itemUIP.pop(item, None)
            self.itemUIV.pop(item, None)
            self.itemUIG.pop(item, None)
            self.tpItem.delete(self.tpItem.curselection())
            self.controller.cRemoveItemL(item)

    def addDataItem(self, pItem: str, pPreis: int, pVersion: str, pOperator: str): #Item aus dem Speicher der GUI hinzufügen
        self.tpItem.insert("end", pItem)
        self.itemUIP[pItem] = pPreis
        self.itemUIV[pItem] = pVersion
        self.itemUIG[pItem] = pOperator
        self.controller.cSetItemL(pItem)

    def addItem(self): #Item der Listbox hinzufügen
        item = self.tpEntry.get()

        if len(item) != 0 and self.goldEntry.get() and self.silberEntry.get() and self.bronzeEntry.get() and self.controller.cGetID(item) is not None:
            self.tpItem.insert("end", item)
            self.itemUIP[item] = self.controller.cConvertGtoC(int(self.goldEntry.get()), int(self.silberEntry.get()), int(self.bronzeEntry.get()))
            self.controller.cSetItemL(item)
            self.itemUIV[item] = "Buy" if self.v.get() == 1 else "Sell"
            self.itemUIG[item] = "Größer" if self.g.get() == 1 else "Kleiner"

        self.tpEntry.delete(0, "end")

    def boxUpdate(self): #Item + Preis + Art der Order anzeigen
        try:
            if self.tpItem.curselection():
                currency = self.controller.cConvertCtoG(self.itemUIP[self.tpItem.get((self.tpItem.curselection()))])
                order = self.itemUIV[self.tpItem.get((self.tpItem.curselection()))]
                operator = self.itemUIG[self.tpItem.get(self.tpItem.curselection())]
                self.b.set("{} Gold {} Silber {} Bronze \nOrder: {} \nOperator: {}".format(currency[0], currency[1], currency[2], order, operator))
        except ValueError and KeyError:
            pass

        self.main.after(450, self.boxUpdate)

    def priceLoop(self, pIndex: int): #ForLoop Alternative für priceUpdate()
        time = self.updateOption.current() + 1

        try:
            self.main.after(int((60000 * time) / len(self.itemUIP)), self.priceUpdate, pIndex + 1)
        except ZeroDivisionError:
            self.main.after(60000 * time, self.priceUpdate, pIndex + 1)

    def priceUpdate(self, pIndex: int): #Get Preis und vergleiche ihn
        if pIndex + 1 > len(self.itemUIP):
            pIndex = 0
        try:
            preisTP = self.controller.cGetPreise(list(self.itemUIP)[pIndex], self.itemUIV[list(self.itemUIV)[pIndex]])
            preisItem = self.itemUIP[list(self.itemUIP)[pIndex]]
            op = self.itemUIG[list(self.itemUIV)[pIndex]]
            if pIndex + 1 <= len(self.itemUIP) and preisItem <= preisTP and op == "Größer":
                self.controller.cNoti(list(self.itemUIP)[pIndex], self.itemUIP[list(self.itemUIP)[pIndex]],
                                      self.itemUIV[list(self.itemUIV)[pIndex]], op)
            elif pIndex + 1 <= len(self.itemUIP) and preisItem >= preisTP and op == "Kleiner":
                self.controller.cNoti(list(self.itemUIP)[pIndex], self.itemUIP[list(self.itemUIP)[pIndex]],
                                      self.itemUIV[list(self.itemUIV)[pIndex]], op)
        except TypeError and IndexError:
            pass

        self.main.after(1000, self.priceLoop, pIndex)

    def getMain(self): #Return main
        return self.main


