from datetime import datetime
ranking=(10,8,6,4,2,0)
projecao = ("crítica","muito aumentada","aumentada","diminuta","improvável","remota")

def predicao(df,ativo,distancia):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    retorno ={}
    r1 = regra1(distancia)
    retorno["ranking"] = ranking[r1]
    retorno["projecao"] = projecao[r1]
    retorno["data"] = dt_string
    return retorno

def get_proc_cognitivo():
 #TODO implementar integração com o modelo
 #['radiacao_global_KJm2','vent_dir','vento_vel','precip_mm','umid_rel_ar','tem_pto_orv','temp_ar_bulbo_seco','press_atm']

    return None

def regra1(dist):
    if dist["distancia"] < 10:
        return 0
    if dist["distancia"] >= 10 and dist["distancia"] < 20:
        return 1
    if dist["distancia"] >= 20 and dist["distancia"] < 50  :
        return 2
    if dist["distancia"] >= 50 and dist["distancia"] < 100  :
        return 3
    if dist["distancia"] >= 100 and dist["distancia"] < 200  :
        return 4
    if dist["distancia"] >= 200:
        return 5