import requests

def get_weather(lat,lon):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"lat":lat,"lon":lon,"units":"%22metric%22 or %22imperial%22","mode":"xml%2C html"}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key':
        }
    retorno = None
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        retorno = response.json()
    except:
        print("Esgotamento de limites de chamada.")
    return retorno