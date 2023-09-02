import geopandas 
import geodatasets 
import matplotlib.pyplot as plt

# nybb = geopandas.read_file(geodatasets.get_path("nybb"))
# chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
# groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries")).explode(ignore_index=True)

# nybb.to_file('data/nybb.geojson', driver='GeoJSON')
# chicago.to_file('data/chicago.geojson', driver='GeoJSON')
# groceries.to_file('data/groceries.geojson', driver='GeoJSON')

nybb = geopandas.read_file("data/nybb.geojson")
chicago = geopandas.read_file("data/chicago.geojson")
groceries = geopandas.read_file("data/groceries.geojson").explode(ignore_index=True)

# this method is designed to work within jupyter notebooks.
nybb.explore()
plt.show()
