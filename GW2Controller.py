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

a = Controller()
a.getGUI().main.mainloop()