import geodatasets 
import geopandas
import pandas as pd 

# chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
# groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))
# chicago.to_file('data/chicago.geojson', driver='GeoJSON')
# groceries.to_file('data/groceries.geojson', driver='GeoJSON')

chicago = geopandas.read_file('data/chicago.geojson')
groceries = geopandas.read_file('data/groceries.geojson')

# we'll use these for attribute joins
chicago_shapes = chicago[['geometry', 'NID']]
chicago_names = chicago[['community', 'NID']]

# we'll use this for a spatial join 
chicago = chicago[['geometry', 'community']].to_crs(groceries.crs)

# appending a geoseries...
joined = pd.concat([chicago.geometry, groceries.geometry])

# appending geodataframes 
douglas = chicago[chicago.community == 'DOUGLAS']
oakland = chicago[chicago.community == 'OAKLAND']
douglas_oakland = pd.concat([douglas, oakland])

# ATTRIBUTE JOINS 

