import geopandas as gpd
from shapely.ops import nearest_points
from shapely.geometry import Point, MultiPoint

from geopy import distance

def get_distancia(df,coodenadas):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
    origem = gpd.points_from_xy(y=[coodenadas['address']['coordinates'][0][0]],
                                x=[coodenadas['address']['coordinates'][0][1]])
    destinos  =  MultiPoint(gdf.geometry.values)
    nearest_geoms = nearest_points(origem[0],destinos)
    fire_lat = nearest_geoms[1].y
    fire_lon = nearest_geoms[1].x
    retorno = {}
    retorno["distancia"]= distance.distance((nearest_geoms[0].y,nearest_geoms[0].x),
                                            (nearest_geoms[1].y,nearest_geoms[1].x)).km
    retorno["geometry"]= {"type": "Point","coordinates": [fire_lat,fire_lon]}
    return retorno