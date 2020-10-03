import geojson
import os
from pymongo import MongoClient
import dns
from bson.objectid import ObjectId
import json

scon = "mongodb+srv://admin:adminadmin@cluster0.5oigr.gcp.mongodb.net/nasa-space-apps-challenge?w=majority"

def cadastrar_ou_retornar_ativo(id,gjson):
    client = MongoClient(scon)
    base_estatistica = client.statistical_skope
    resultado = base_estatistica.ativos.find({"identificador":id}).sort("_id",-1).limit(1)
    if resultado.count() == 0:
        gjson["identificador"]=  id
        unico = base_estatistica.ativos.insert_one(gjson)
        retorno = (200,"Ativo "+str(id)+" cadastrado com sucesso!")
    else:
        retorno = (409,"Ativo anteriormente cadastrado.")
    client.close()
    return retorno

def inferencia(id):
    if id ==1 :
        i = "./mock/Incendio1.json"
    else:
        i = "./mock/Incendio2.json"
    with open(i) as f:
        gj = geojson.load(f)
    return gj