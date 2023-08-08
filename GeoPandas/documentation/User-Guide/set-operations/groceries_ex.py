from geodatasets import get_path
from geopandas import read_file
import matplotlib.pyplot as plt

# chicago = read_file(get_path("geoda.chicago_commpop"))
# groceries = read_file(get_path("geoda.groceries"))
chicago = read_file("data/chicago_compop.geojson")
groceries = read_file("data/groceries.geojson")

# write to files 
# chicago.to_file("data/chicago_compop.geojson")
# groceries.to_file("data/groceries.geojson")

# Project to crs that uses meters as distance measure
chicago = chicago.to_crs("ESRI:102003")
groceries = groceries.to_crs("ESRI:102003")

chicago.plot()
plt.show()

