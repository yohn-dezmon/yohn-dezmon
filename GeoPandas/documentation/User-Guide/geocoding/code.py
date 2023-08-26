import geopandas
import geodatasets
import matplotlib.pyplot as plt

boros = geopandas.read_file(geodatasets.get_path("nybb"))

boros.BoroName

# retuns a GeoDataFrame of geometry (Point()) and address
# borough, city, state, country
boro_locations = geopandas.tools.geocode(boros.BoroName)
print(boro_locations)

import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
boros.to_crs("EPSG:4326").plot(ax=ax, color="white", edgecolor="black")
boro_locations.plot(ax=ax, color="red");

plt.show()
