from datetime import date
from application.models.entity.medicoes import Medicoes

lista_medicao = [Medicoes(1, 20.0, 50, 0.2, 5.5, 0.01, 0.02, '15/06/2020'), Medicoes(2, 50.5, 30, 0.7, 1.5, 0.15, 5.2, '11/06/2020')]
lista_dict_medicao = []

class MedicoesDao():
    def __init__(self):
        self.lista_medicao = lista_medicao
        self.lista_dict_medicao = lista_dict_medicao

    def get_lista_medicao(self):
        return self.lista_medicao

    def lista_to_dict(self):
        lista = []
        for medicao in lista_medicao:
            lista.append(medicao.toDict())
        return lista