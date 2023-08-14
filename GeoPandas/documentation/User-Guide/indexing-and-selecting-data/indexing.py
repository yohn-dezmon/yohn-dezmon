from geodatasets import get_path
from geopandas import read_file
import matplotlib.pyplot as plt

# chile = read_file(get_path('geoda.chile_labor'))
# chile.to_file("data/chile_labor.geojson" , driver="GeoJSON")

chile = read_file("data/chile_labor.geojson")
# chile.plot(figsize=(8, 8))


# I think cx is (longitude, latitude)

# display the bottom 50 latitude points 
southern_chile = chile.cx[:, :-50]
southern_chile.plot(figsize=(8, 8))
plt.show()
