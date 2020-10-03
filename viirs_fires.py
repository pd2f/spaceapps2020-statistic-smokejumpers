import pandas as pd
url_mock = "./mock/mock_20200505.pickle"
#TODO criar serviços para obter dados do viirs
df = pd.read_pickle(url_mock)
def get_VIIRS_data():
    return df;

