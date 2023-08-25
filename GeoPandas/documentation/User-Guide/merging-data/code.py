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
print(chicago_shapes.head())
print(chicago_names.head())

chicago_shapes = chicago_shapes.merge(chicago_names, on='NID')
print(chicago_shapes.head())


# SPATIAL JOINS 
# both geodataframes have geometry columns!

# one geodataframe of communities, one of grocery stores. 
# want to merge to get each grocery's community.
print(chicago.head())
print(groceries.head())

# spatial join! (`sjoin()`)
# predicate = intersects! 
groceries_with_community = groceries.sjoin(chicago, how='inner', predicate='intersects')
print(groceries_with_community.head())

