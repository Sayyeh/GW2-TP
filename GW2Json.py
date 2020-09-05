import json

class GW2Json:

    def __init__(self):
        pass

    @staticmethod
    def jsonCreate(pItemLP, pItemLV):
        data = {"Preise": pItemLP, "Versionen": pItemLV}

        with open("Json/data.json", "w") as outfile:
            json.dump(data, outfile, indent = 2)

    @staticmethod
    def jsonRead():
        try:
            with open("Json/data.json", "r+") as fi:
                f = json.load(fi)
                itemP = f["Preise"]
                itemV = f["Versionen"]
        except json.decoder.JSONDecodeError:
            itemP = {}
            itemV = {}

        return itemP, itemV
