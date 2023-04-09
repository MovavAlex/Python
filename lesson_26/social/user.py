import requests

class User:
    def __init__(self, name="", surname="", password="", login=""):
        self.__data = requests.get('https://api.randomdatatools.ru/').json()
        self.login = self.__data["Login"] if not login else login
        self.__password = self.__data["Password"] if not password else password
        self.name = self.__data["FirstName"] if not name else name
        self.surname = self.__data["LastName"] if not surname else surname
        self.subscribes = []
        self.subscribers = []

    def log_in(self, l, p):
        if l == self.login and p == self.__password:
            return True
        else:
            return False
