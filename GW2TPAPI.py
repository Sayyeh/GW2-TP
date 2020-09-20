import requests as re

class WrongStatus(Exception):
    pass

class GW2API:

    def __init__(self, pAPI: str = None):
        self.api = pAPI
        self.baseurl = "https://api.guildwars2.com"
        self.version = "/v2/"

    def setAPI(self, pAPI: str): #Setzen der API
        self.api = pAPI

    def getCommerceprices(self, pId: str): #Call an die API für buy und sell Preise
        url = "commerce/prices/"
        response = re.get(self.baseurl + self.version + url + pId)
        status = response.status_code

        if status == 200:
            return response.json() #19976
        else:
            raise WrongStatus("Seite kann nicht erreicht werden")

# a = GW2API()
# b = a.getCommerceprices("19976")
# print(b)