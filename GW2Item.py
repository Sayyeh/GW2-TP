class GW2Item:

    def __init__(self, pName: str, pPreis: int, pVersion: str, pOperator: str, pMehrmals: bool = True):
        self.Name = pName
        self.Preis = pPreis
        self.Version = pVersion
        self.Operator = pOperator
        self.Id = None
        self.Mehrmals = pMehrmals
        self.nochmal = True

    def setId(self, pId: str):
        self.Id = pId

    def setNochmal(self, pN: bool):
        self.nochmal = pN

    def setAnzahl(self, pMehrmals: bool):
        self.Mehrmals = pMehrmals

    def getName(self):
        return self.Name

    def getVersion(self):
        return self.Version

    def getOP(self):
        return self.Operator

    def getId(self):
        return self.Id

    def getPreis(self):
        return self.Preis

    def getNochmal(self):
        return self.nochmal

    def getMehrmals(self):
        return self.Mehrmals