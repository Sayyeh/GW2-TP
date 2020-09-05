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
        self.widgets = []
        self.imgGold = tk.PhotoImage(file = "Images/Gold_coin.png")
        self.imgSilber = tk.PhotoImage(file = "Images/Silver_coin.png")
        self.imgBronze = tk.PhotoImage(file = "Images/Copper_coin.png")
        self.v = tk.IntVar()
        self.b = tk.StringVar()
        self.u = tk.StringVar()

        self.apiButton = tk.Button(self.main, text = "API-Key eingeben", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "disabled",
                                   disabledforeground= "#494a49", command = self.startAPI)
        self.apiButton.place(x = 0, y = 0)

        self.apiEntry = tk.Entry(self.main, bg = "#1c1d1c", fg = "#EEE9E9", width = 75, bd = 0, state = "disabled", disabledbackground = "#494a49", disabledforeground= "#EEE9E9")
        self.apiEntry.place(x = 0, y = 25)

        self.apiChange = tk.Button(self.main, text = "Change", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0,
                                   disabledforeground= "#494a49", command = self.changeAPIstate)
        self.apiChange.place(x = 395, y = 0)

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

        self.priceUpdate(0)

    def readItem(self):
        temp = self.controller.cReadItem()

        if temp[0] and temp[1]:
            for i in temp[0]:
                self.addDataItem(i, temp[0][i], temp[1][i])

    def saveItem(self):
        self.controller.cSaveItem(self.itemUIP, self.itemUIV)

    def getItemLP(self):
        return self.itemUIP

    def getItemLV(self):
        return self.itemUIV

    def startAPI(self): #API übertrangen und WIdgets entsperren
        self.controller.cSetAPI(self.apiEntry.get())

        if len(self.apiEntry.get()) != 0:
            self.apiEntry.delete(0, "end")

            self.widgets = [self.apiChange, self.tpItem, self.tpButton, self.tpEntry, self.goldEntry, self.goldT,
                            self.silberEntry, self.silberT, self.bronzeEntry, self.bronzeT, self.buyRadio,
                            self.sellRadio, self.tpRemove, self.updateOption, self.saveButton]

            self.apiEntry.config(state = "disabled")
            self.apiButton.config(state = "disabled")
            for i in self.widgets:
                i.config(state = "normal")
            self.v.set(1)
            self.updateOption["values"] = ["1 min", "2 min", "3 min", "4 min", "5 min"]
            self.u.set("1 min")
            self.boxUpdate()
            self.readItem()

    def removeItem(self): #Item aus der Listbox entfernen
        if self.tpItem.curselection():
            item = self.tpItem.get(self.tpItem.curselection())
            self.itemUIP.pop(item, None)
            self.itemUIV.pop(item, None)
            self.tpItem.delete(self.tpItem.curselection())
            self.controller.cRemoveItemL(item)

    def changeAPIstate(self): #API-Eingabefeld entsperren
        self.apiEntry.config(state="normal")
        self.apiButton.config(state="normal")

    def addDataItem(self, pItem, pPreis, pVersion):
        self.tpItem.insert("end", pItem)
        self.itemUIP[pItem] = pPreis
        self.itemUIV[pItem] = pVersion
        self.controller.cSetItemL(pItem)

    def addItem(self): #Item der Listbox hinzufügen
        item = self.tpEntry.get()

        if len(item) != 0 and self.goldEntry.get() and self.silberEntry.get() and self.bronzeEntry.get():
            self.tpItem.insert("end", item)
            self.tpEntry.delete(0, "end")
            self.itemUIP[item] = self.controller.cConvertGtoC(int(self.goldEntry.get()), int(self.silberEntry.get()), int(self.bronzeEntry.get()))
            self.controller.cSetItemL(item)
            if self.v.get() == 1:
                self.itemUIV[item] = "Buy"
            else:
                self.itemUIV[item] = "Sell"

    def boxUpdate(self): #Item + Preis + Art der Order anzeigen
        try:
            if self.tpItem.curselection():
                currency = self.controller.cConvertCtoG(self.itemUIP[self.tpItem.get((self.tpItem.curselection()))])
                order = self.itemUIV[self.tpItem.get((self.tpItem.curselection()))]
                self.b.set("{} Gold {} Silber {} Bronze \n{}".format(currency[0], currency[1], currency[2], order) + "order")
        except ValueError and KeyError:
            pass

        self.main.after(500, self.boxUpdate)

    def priceLoop(self, pIndex):
        time = self.updateOption.current() + 1

        self.main.after(60000 * time, self.priceUpdate, pIndex + 1)

    def priceUpdate(self, pIndex):
        if pIndex + 1 > len(self.itemUIP):
            pIndex = 0
        try:
            print(self.itemUIP[list(self.itemUIP)[pIndex]])
            if pIndex + 1 <= len(self.itemUIP) and self.itemUIP[list(self.itemUIP)[pIndex]] >= self.controller.cGetPreise(list(self.itemUIP)[pIndex], self.itemUIV[list(self.itemUIV)[pIndex]]):
                self.controller.cNoti(list(self.itemUIP)[pIndex], self.itemUIP[list(self.itemUIP)[pIndex]])
        except TypeError and IndexError:
            pass

        self.main.after(1000, self.priceLoop, pIndex)


