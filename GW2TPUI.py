import tkinter as tk
from tkinter import ttk
from GW2TPAPI import WrongStatus

class GW2GUI:

    def __init__(self, pController):
        self.started = False
        self.main = tk.Tk()
        self.main.title("Gw2 Alarm")
        self.main.geometry("495x495+0+0")
        self.main.resizable(False, False)
        self.main.configure(background="#383a39")
        self.main.iconbitmap("Images/icon.ico")
        self.controller = pController
        self.itemUIP = [] #Liste der Items
        self.imgGold = tk.PhotoImage(file = "Images/Gold_coin.png")
        self.imgSilber = tk.PhotoImage(file = "Images/Silver_coin.png")
        self.imgBronze = tk.PhotoImage(file = "Images/Copper_coin.png")
        self.v = tk.IntVar() #Buy/Sell Order
        self.g = tk.IntVar() #Operator
        self.a = tk.IntVar() #Annzahl der Alarme
        self.b = tk.StringVar() #Anzeige Text beim Auswählen eines Items
        self.u = tk.StringVar() #Updatetimer
        self.d = tk.StringVar() #Dauer der Win10 Notification

        self.title = tk.Label(self.main, text = "GW2 P E P E G A ", font = ("Verdanan", 21, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                               activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0)
        self.title.place(x = 0, y = 0)

        self.ladenButton = tk.Button(self.main, text = "Laden", font = ("Verdanan", 11, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                      activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "normal",
                                      disabledforeground= "#494a49", command = self.laden)
        self.ladenButton.place(x = 0, y = 35)

        self.tpItem = tk.Listbox(self.main, bg = "#1c1d1c", font = ("Verdanan", 10, "bold"), bd = 0, highlightthickness = 0, selectbackground = "#ce480f", fg = "white")
        self.tpItem.place(x = 0, y = 60)

        self.tpButton = tk.Button(self.main, text = "Item hinzufügen", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "normal",
                                   disabledforeground= "#494a49", command = self.addItem)
        self.tpButton.place(x = 140, y = 60)

        self.tpRemove = tk.Button(self.main, text = "Item löschen", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                   activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "normal",
                                   disabledforeground= "#494a49", command = self.removeItem)
        self.tpRemove.place(x = 353, y = 60)


        self.tpEntry = tk.Entry(self.main, bg = "#1c1d1c", fg = "#EEE9E9", width = 50, bd = 0, state = "normal", disabledbackground = "#494a49", disabledforeground= "#EEE9E9")
        self.tpEntry.place(x = 140, y = 85)

        self.goldEntry = tk.Entry(self.main, bg="#1c1d1c", fg="#EEE9E9", width=4, bd=0, state="normal", disabledbackground="#494a49", disabledforeground="#EEE9E9")
        self.goldEntry.place(x = 140, y = 102)

        self.goldT = tk.Label(self.main, image = self.imgGold, bg = "#383a39")
        self.goldT.place(x = 167, y = 102)

        self.silberEntry = tk.Entry(self.main, bg="#1c1d1c", fg="#EEE9E9", width=4, bd=0, state="normal", disabledbackground="#494a49", disabledforeground="#EEE9E9")
        self.silberEntry.place(x = 190, y = 102)

        self.silberT = tk.Label(self.main, image = self.imgSilber, bg = "#383a39")
        self.silberT.place(x = 217, y = 102)

        self.bronzeEntry = tk.Entry(self.main, bg="#1c1d1c", fg="#EEE9E9", width=4, bd=0, state="normal", disabledbackground="#494a49", disabledforeground="#EEE9E9")
        self.bronzeEntry.place(x = 240, y = 102)

        self.bronzeT = tk.Label(self.main, image = self.imgBronze, bg = "#383a39")
        self.bronzeT.place(x = 267, y = 102)

        self.buyRadio = tk.Radiobutton(self.main, text = "Buy order", variable = self.v, value = 1, bg = "#383a39", fg = "#EEE9E9",
                                        activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "normal")
        self.buyRadio.place(x = 140, y = 120)

        self.sellRadio = tk.Radiobutton(self.main, text = "Sell order", variable = self.v, value = 2, bg = "#383a39", fg = "#EEE9E9",
                                         activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "normal")
        self.sellRadio.place(x = 140, y = 138)

        self.boxInfo = tk.Label(self.main, textvariable = self.b, font = ("Verdanan", 10, "bold"), bg="#383a39", fg="#EEE9E9")
        self.boxInfo.place(x =  140, y = 200)

        self.updateOption = ttk.Combobox(self.main, textvariable = self.u, state = "normal")
        self.updateOption.place(x = 0, y = 233)
        self.updateOption.bind("<Key>", lambda e: "break")

        self.delayOption = ttk.Combobox(self.main, textvariable = self.d, state = "normal")
        self.delayOption.place(x = 0, y = 293)
        self.delayOption.bind("<Key>", lambda e: "break")
        self.delayOption.bind("<<ComboboxSelected>>", self.setDelay)

        self.updateLabel = tk.Label(self.main, text = "Wie oft soll geupdated \nwerden?", font = ("Verdanan", 9, "bold"), bg="#383a39", fg="#EEE9E9")
        self.updateLabel.place(x = 0, y = 255)

        self.delayLabel = tk.Label(self.main, text = "Wie lange \nsollen Benachrichtungen \nangezeigt werden?", font = ("Verdanan", 9, "bold"), bg="#383a39", fg="#EEE9E9")
        self.delayLabel.place(x = 0, y = 315)

        self.saveButton = tk.Button(self.main, text = "Speichern", font = ("Verdanan", 10, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                     activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "normal",
                                     disabledforeground= "#494a49", command = self.saveItem)
        self.saveButton.place(x = 368, y = 104)

        self.biggerRadio = tk.Radiobutton(self.main, text = "TP Preis größer", variable = self.g, value = 1, bg = "#383a39", fg = "#EEE9E9",
                                           activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "normal")
        self.biggerRadio.place(x = 220, y = 120)

        self.smallerRadio = tk.Radiobutton(self.main, text = "TP Preis kleiner", variable = self.g, value = 2, bg = "#383a39", fg = "#EEE9E9",
                                            activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "normal")
        self.smallerRadio.place(x = 220, y = 138)

        self.einmaligRadio = tk.Radiobutton(self.main, text = "Einmaliger Alarm", variable = self.a, value = 1, bg = "#383a39", fg = "#EEE9E9",
                                           activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "normal")
        self.einmaligRadio.place(x = 140, y = 160)

        self.mehrRadio = tk.Radiobutton(self.main, text = "Mehrmaliger Alarm", variable = self.a, value = 2, bg = "#383a39", fg = "#EEE9E9",
                                            activebackground = "#383a39", activeforeground = "#EEE9E9", selectcolor = "#1c1d1c", state = "normal")
        self.mehrRadio.place(x = 140, y = 178)

        self.reaktButton = tk.Button(self.main, text = "Reaktivieren", font = ("Verdanan", 9, "bold"), bg="#1c1d1c", fg="#EEE9E9",
                                     activeforeground = "#ce480f", activebackground = "#1c1d1c", relief = "flat", bd = 0, state = "normal",
                                     disabledforeground= "#494a49", command = self.reaktivierenItem)
        self.reaktButton.place(x = 270, y = 162)

        self.main.bind("<Return>", self.addItem)

        self.priceUpdate(0)
        self.startGUI()

    def reaktivierenItem(self):
        if self.tpItem.curselection():
            item = self.controller.cGetItem(self.tpItem.get((self.tpItem.curselection())))
            item.setNochmal(True)

    def readItem(self, pIndex = 0): #Lese Items aus dem Speicher
        temp = self.controller.cReadItem()

        if temp and pIndex + 1 <= len(temp): #Items werden der Reihe nach geladen
            i = list(temp)[pIndex]
            self.addDataItem(i, temp[i]["Preis"], temp[i]["Version"], temp[i]["Operator"], temp[i]["Mehrmals"])

            self.main.after(10, self.readItem, pIndex + 1)

    def saveItem(self): #Speichere Items in den Spreicher
        self.controller.cSaveItem()

    def laden(self):
        if self.tpItem.size() == 0:  #Wenn was im Speicher, lade ihn
            self.readItem()

    def startGUI(self): #GUI starten und entsperren (war früher startAPI())
        if not self.started:
            self.started = True
            self.v.set(1)
            self.g.set(1)
            self.a.set(2)
            self.updateOption["values"] = ["1 min", "2 min", "3 min", "4 min", "5 min"]
            self.delayOption["values"] = ["25 sec", "20 sec", "15 sec", "10 sec"]
            self.u.set("2 min")
            self.d.set("20 sec")
            self.boxUpdate()

    def removeItem(self): #Item aus der Listbox entfernen
        if self.tpItem.curselection():
            item = self.tpItem.get(self.tpItem.curselection())
            self.itemUIP.remove(item)
            self.tpItem.delete(self.tpItem.curselection())
            self.controller.cRemoveItemL(item)

    def addDataItem(self, pItem: str, pPreis: int, pVersion: str, pOperator: str, pAnzahl): #Item aus dem Speicher der GUI hinzufügen
        self.tpItem.insert("end", pItem)
        self.itemUIP.append(pItem)
        self.controller.cSetItemL(pItem, pPreis, pVersion, pOperator, pAnzahl)

    def addItem(self, event = None): #Item der Listbox hinzufügen
        item = self.tpEntry.get()

        if len(item) != 0 and self.goldEntry.get() and self.silberEntry.get() and self.bronzeEntry.get() and\
        self.controller.cGetID(item) is not None:
            self.tpItem.insert("end", item)
            preis = self.controller.cConvertGtoC(int(self.goldEntry.get()), int(self.silberEntry.get()),
                                                 int(self.bronzeEntry.get()))
            version = "Buy" if self.v.get() == 1 else "Sell"
            op = "Größer" if self.g.get() == 1 else "Kleiner"
            nochmal = False if self.a.get() == 1 else True
            self.controller.cSetItemL(item, preis, version, op, nochmal)
            self.itemUIP.append(item)

        self.tpEntry.delete(0, "end")

    def boxUpdate(self): #Item + Preis + Art der Order anzeigen
        try:
            if self.tpItem.curselection():
                item = self.controller.cGetItem(self.tpItem.get((self.tpItem.curselection())))
                currency = self.controller.cConvertCtoG(item.getPreis())
                order = item.getVersion()
                operator = item.getOP()
                self.b.set("{} Gold {} Silber {} Bronze \nOrder: {} \nOperator: {}".format(currency[0], currency[1],
                                                                                           currency[2], order, operator))
                if not item.getNochmal(): #Ignore this pls
                    self.reaktButton.config(state = "normal")
                else:
                    self.reaktButton.config(state="disabled")
            else:
                self.reaktButton.config(state="disabled")
                self.b.set("")
        except (ValueError, KeyError) as e:
            pass

        self.main.after(350, self.boxUpdate)

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
            item = self.controller.cGetItem(self.itemUIP[pIndex])
            version = item.getVersion()
            preisTP = self.controller.cGetPreise(item.getName(), version)
            preisItem = item.getPreis()
            op = item.getOP()
            if pIndex + 1 <= len(self.itemUIP) and (preisItem <= preisTP and op == "Größer")\
            or (preisItem >= preisTP and op == "Kleiner") and item.getNochmal():
                self.controller.cNoti(item.getName(), preisItem, version, op)
                if not item.getMehrmals():
                    item.setNochmal(False)
        except (WrongStatus, IndexError, TypeError) as e:
            pass

        self.main.after(1000, self.priceLoop, pIndex)

    def getMain(self): #Return main
        return self.main

    def setDelay(self, event): #Delay übergeben
        self.controller.cSetDelay(int(self.d.get()[0:2]))
