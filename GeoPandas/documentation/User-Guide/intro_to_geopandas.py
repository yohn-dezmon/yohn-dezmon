"""
Reading and writing files
"""

import geopandas 
from geodatasets import get_path 

# a map of New York boroughs
# path_to_data = get_path("nybb")
gdf = geopandas.read_file("data/nybb.geojson")

print(gdf)

# .geojson
# gdf.to_file("data/nybb.geojson", driver="GeoJSON")
