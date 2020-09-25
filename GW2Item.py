class GW2Item:

    def __init__(self, pName: str, pPreis: int, pVersion: str, pOperator: str, pMehrmals: bool = False):
        self.Name = pName
        self.Preis = pPreis
        self.Version = pVersion
        self.Operator = pOperator
        self.Id = None
        self.Mehrmals = pMehrmals

    def setId(self, pId: str):
        self.Id = pId

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