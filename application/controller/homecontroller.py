from datetime import datetime
from application import app
from flask import request, jsonify
from application.models.entity.medicoes import Medicoes
from application.models.dao.medicoesDAO import MedicoesDao

medicoesDao = MedicoesDao()
lista_medicao = medicoesDao.get_lista_medicao()
lista_dict_medicao = medicoesDao.lista_to_dict()

@app.route("/medicoes", methods=['GET'])
def medicoes():
    return jsonify(lista_dict_medicao)


@app.route("/medicoes", methods=['POST'])
def addMed():
    med = request.json
    medicao = Medicoes(
        med["id"],
        med["temp"],
        med["umid"],
        med["ozonio"],
        med["matPart"],
        med["co"],
        med["n2o"],
        med["data"]
    )
    lista_dict_medicao.append(medicao.toDict())
    return jsonify(lista_dict_medicao)


@app.route("/medicoes/id/<id>")
def filtrarId(id):
    lista_filtro = []
    for medicao in lista_dict_medicao:
        if medicao["id"] == int(id):
            lista_filtro.append(medicao)
    
    return jsonify(lista_filtro)

@app.route("/medicoes/data/<data>")
def filtrarData(data):
    lista_filtro = []
    print(lista_dict_medicao)
    for medicao in lista_dict_medicao:
        datajson = medicao["data"].replace("/", "")
        print(datajson)
        if datajson == data:
            lista_filtro.append(medicao)

    return jsonify(lista_filtro)


#identificador dos medidores, converter data com strptime 