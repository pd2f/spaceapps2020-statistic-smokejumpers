import pandas as pd
from bs4 import BeautifulSoup
import requests

class DataVIIRS:
    def __init__(self):
        self.auth =
        self.url_base = "https://nrt3.modaps.eosdis.nasa.gov"
        self.url_recursos = self.url_base+'/api/v2/content/archives/FIRMS/viirs/South_America'
        self.url_destino = "./data_viirs/"
        self.url_data_viirs = "./data_viirs/data_viirs.pickle"

    def obter_ultimo_arquivo(self):
        res = requests.session()
        data = res.get(self.url_recursos, headers=self.auth)
        dados = BeautifulSoup(data.content, 'html.parser')
        lista = [dd['href'] for dd in dados.html.body.table.find_all('a')]
        lista.sort(reverse=True)
        recurso = res.get(self.url_base+lista[1], headers=self.auth)
        open( self.url_destino+
             recurso.headers.get("Content-Disposition").split("=")[1], 'wb')\
            .write(recurso.content)
        dataset = pd.read_csv(self.url_destino + recurso.headers.get("Content-Disposition").split("=")[1], sep=",")
        dataset.to_pickle(self.url_data_viirs)
        res.close()

    def get_VIIRS_data(self):
        return pd.read_pickle(self.url_data_viirs);

