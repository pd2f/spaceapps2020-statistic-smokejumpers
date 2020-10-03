import pandas as pd
url_mock = "C:\\Users\\Usuario\\Documents\\projetos\\software\\spaceapps2020\\mock\\mock_20200505.pickle"
#TODO criar serviços para obter dados do viirs
df = pd.read_pickle(url_mock)
def get_VIIRS_data():
    return df;

