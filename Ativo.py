import geojson

from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import nearest_fire as nf
import motor_inferencia as inf
import viirs_fires as viirs
import weather

scon =

def data_viirs():
    return viirs.DataVIIRS()

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
    client = MongoClient(scon)
    base_estatistica = client.statistical_skope
    resultado = base_estatistica.ativos.find({"identificador": id}).sort("_id", -1).limit(1)
    result = resultado.next()
    if result["identificador"] == id:
        dados_viirs = viirs.DataVIIRS()
        df = dados_viirs.get_VIIRS_data()
        dist = nf.get_distancia(df,result)
        lat = dist['geometry']['coordinates'][0]
        lon = dist['geometry']['coordinates'][1]
        clima = weather.get_weather(lat=lat, lon=lon)
        predito = inf.predicao(df,result,dist)
        retorno = (200, "Chamada de processamento estatístico não implementada")
    else:
        retorno = (417, "Conflito de ativo, realize o recadastramento do ativo.")
    gj = {}
    gj.update(predito)
    gj.update(dist)
    if clima is not None:
        gj.update(clima)
    return gj