import json

class GW2Json:

    def __init__(self):
        pass

    @staticmethod
    def jsonCreate(pItemL: dict):
        data = {}

        for i in pItemL:
            data[i] = pItemL[i].__dict__
            data[i].pop("nochmal", None)

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
