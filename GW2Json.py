import json

class GW2Json:

    def __init__(self):
        pass

    @staticmethod #{'Mystic Coin': <GW2Item.GW2Item object at 0x052B6250>, 'Bolt': <GW2Item.GW2Item object at 0x076531F0>}
    def jsonCreate(pItemL: dict):
        data = {}

        for i in pItemL:
            data[i] = pItemL[i].__dict__

        with open("Json/data.json", "w") as outfile:
            json.dump(data, outfile, indent = 2)

    @staticmethod
    def jsonRead():
        try:
            with open("Json/data.json", "r+") as fi:
                f = json.load(fi)
        except json.decoder.JSONDecodeError:
            f = {}

        return f
