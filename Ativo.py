import geojson
import os
def cadastrar_ativo(id,gjson):
    return "Ativo cadastrado com sucesso!"

def inferencia(id):
    if id ==1 :
        i = "./mock/Incendio1.json"
    else:
        i = "./mock/Incendio2.json"
    with open(i) as f:
        gj = geojson.load(f)
    return gj