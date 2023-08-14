from geodatasets import get_path
from geopandas import read_file
import matplotlib.pyplot as plt

# chicago = read_file(get_path("geoda.chicago_commpop"))
# groceries = read_file(get_path("geoda.groceries"))
chicago = read_file("data/chicago_compop.geojson")
groceries = read_file("data/groceries.geojson")

# write to files 
# chicago.to_file("data/chicago_compop.geojson", driver="GeoJSON")
# groceries.to_file("data/groceries.geojson", driver="GeoJSON")

# Project to crs that uses meters as distance measure
chicago = chicago.to_crs("ESRI:102003")
groceries = groceries.to_crs("ESRI:102003")

# chicago.plot()
# plt.show()

# buffer all grocery geometries by 1 km 
groceries['geometry']= groceries.buffer(1000)
groceries.plot()
plt.show()
# get the intersecting areas of chicago with the buffered groceries 
chicago_cores = chicago.overlay(groceries, how='intersection')
chicago_cores.plot(alpha=0.5, edgecolor='k', cmap='tab10')

"""
Not sure why but I'm unable to view the groceries data
it only works if I dl it from the library
"""
