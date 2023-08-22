import geopandas
import geodatasets
import matplotlib.pyplot as plt 

# nepal = geopandas.read_file(geodatasets.get_path('geoda.nepal'))
# nepal.to_file("data/nepal.geojson" , driver="GeoJSON")

nepal = geopandas.read_file("data/nepal.geojson")
# at first each row corresopnds to a district which has a zone column
# the zone column is originally called "name_2"
nepal = nepal.rename(columns={"name_2": "zone"})
print(nepal[["zone", "geometry"]].head())

nepal_zone = nepal[['zone', 'geometry']]
# how we should have one geometry per zone I think
zones = nepal_zone.dissolve(by='zone')
print(zones.head())

# getting aggregate population per zone! 
nepal_pop = nepal[['zone', 'geometry', 'population']]
zones = nepal_pop.dissolve(by='zone', aggfunc='sum')
# zones.plot(column='population', scheme='quantiles', cmap='YlOrRd')
# plt.show()
print(zones.head())

# example of using the dict of axis labels 
zones = nepal.dissolve(
    by="zone",
    aggfunc={
        "district": "count",
        "population": ["min", "max"],
    },
)
print(zones.head())
