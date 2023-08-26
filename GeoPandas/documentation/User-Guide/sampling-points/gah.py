import geopandas
import geodatasets

# nybb = geopandas.read_file(geodatasets.get_path("nybb"))
# nybb.to_file('data/nybb.geojson', provider='GeoJSON')


nybb = geopandas.read_file("data/nybb.geojson")
# simplify geometry to save sapce wehn rendering many interactive maps...
