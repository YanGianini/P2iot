
class Medicoes():
    def __init__(self, temp, umid, ozonio, matPart, co, n2o):
        self.__temp = temp
        self.__umid = umid
        self.__ozonio = ozonio
        self.__matPart = matPart
        self.__co = co
        self.__n2o = n2o


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
        self.__n20 = n2o
