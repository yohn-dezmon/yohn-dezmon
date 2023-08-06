"""
Reading and writing files
"""

import geopandas 
from geodatasets import get_path 

# a map of New York boroughs
path_to_data = get_path("nybb")
# "data/nybb.geojson"
gdf = geopandas.read_file(path_to_data)

print(gdf)

# .geojson
gdf.to_file("data/nybb.geojson", driver="GeoJSON")
