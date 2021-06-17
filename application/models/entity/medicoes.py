
from datetime import datetime


class Medicoes():
    def __init__(self,id: int, temp: float, umid: int, ozonio: float, matPart: float, co: float, n2o: float, data: datetime):
        self.__id = id
        self.__temp = temp
        self.__umid = umid
        self.__ozonio = ozonio
        self.__matPart = matPart
        self.__co = co
        self.__n2o = n2o
        self.__data = data

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_temp(self):
        return self.__temp

    def set_temp(self, temp):
        self.__temp = temp


    def get_umid(self):
        return self.__umid

    def set_umid(self, umid):
        self.__umid = umid

    
    def get_ozonio(self):
        return self.__ozonio

    def set_ozonio(self, ozonio):
        self.__ozonio = ozonio

    
    def get_matPart(self):
        return self.__matPart

    def set_matPart(self, matPart):
        self.__matPart = matPart

    
    def get_co(self):
        return self.__co

    def set_co(self, co):
        self.__co = co


    def get_n2o(self):
        return self.__n2o

    def set_n2o(self, n2o):
        self.__n2o = n2o


    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


    def toDict(self):
        return {
            "id": self.__id,
            "temp": self.__temp,
            "umidade": self.__umid,
            "ozonio": self.__ozonio,
            "matPart": self.__matPart,
            "co": self.__co,
            "n2o": self.__n2o,
            "data": self.__data
        }

