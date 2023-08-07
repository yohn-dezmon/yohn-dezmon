"""
Reading and writing files
"""
import geopandas 
import matplotlib.pyplot as plt
from geodatasets import get_path
# folium and mapclassify are requried for .explore()
# pip install folium mapclassify
 

# reading a file
# a map of New York boroughs
path_to_data = get_path("nybb")
# path_to_data
gdf = geopandas.read_file("data/nybb.geojson")

print(gdf)
print(gdf.columns)

# writing to a file
# .geojson
# gdf.to_file("data/nybb.geojson", driver="GeoJSON")

# set names of boroughs as the index
gdf = gdf.set_index("BoroName") 
gdf['area'] = gdf.area
print(gdf['area'].sort_values())

# getting the boundary (LineString) of each polygon
# we now have two geometries in our GeoDataframe (area, boundary)
# in addition to our original 'geometry' column
gdf['boundary'] = gdf.boundary
print(gdf['boundary'])

# creating centroid geometry column
# each centroid is a POINT() geometry
gdf["centroid"] = gdf.centroid


# measuring how far each centroid is from the first centroid location
first_point = gdf["centroid"].iloc[0]
gdf["distance"] = gdf["centroid"].distance(first_point)
print(gdf["distance"].sort_values())

# average distance of each borough from staten island
print(gdf["distance"].mean())


# MAKING MAPS 
# to plot the active geometry, call GeoDataFrame.plot()
# gdf.plot("area", legend=True)
# plt.show()

# view your data interactively 
# gdf.explore("area", legend=False)
# # hm this didn't work with plt.show()...
# plt.show()

# You can switch the active geometry with df.set_geometry()
gdf = gdf.set_geometry("centroid")
# gdf.plot("area", legend=True)
# plt.show()

# layering multiple GeoSeries on top of each other! 
# you have to use one plot as the axis for the other! 
# ax = gdf["geometry"].plot()
# color here becomes the color of the centroids
# ax is the basemap geometry from above
# gdf["centroid"].plot(ax=ax, color="black")
# plt.show()

# we set the geometry back to the original geometry (not sure why...)
gdf = gdf.set_geometry("geometry")


# GEOMETRY CREATION! 
# what is a convex hull? the smallest possible convex polygon containing all the points 
# in the set. (in this case a single borough)
gdf["convex_hull"] = gdf.convex_hull

# set the convex hulls as the axis
# alpha sets the transparency...
# ax = gdf["convex_hull"].plot(alpha=0.5)
# passing the first plot and setting linewidth to 0.5
# gdf["boundary"].plot(ax=ax, color="white", linewidth=0.5)
# plt.show()


# BUFFER!
# buffering the active geometry by 10,000 feet 
gdf["buffered"] = gdf.buffer(10000)
# buffering the centroid geometry by 10,000 feet 
gdf["buffered_centroid"] = gdf["centroid"].buffer(10000)
# saving the first plot as an axis and setting alpha to 0.5
# ax = gdf["buffered"].plot(alpha=0.5)
# # passing the first plot as an axis to the second
# gdf["buffered_centroid"].plot(ax=ax, color='red', alpha=0.5)
# # passing the first plot and setting linewidth to 0.5
# gdf["boundary"].plot(ax=ax, color="white", linewidth=0.5)
# plt.show()

# GEOMETRY RELATIONS

# Q: which of the buffered boroughs intersect with the original geometry of brooklyn
# i.e. which of the boundaries are within 10,000 feet from brooklyn
# first we get Brooklyn's geometry value
brooklyn = gdf.loc["Brooklyn", "geometry"]
# which of the geometries in gdf["buffered"] intersects it.
print(gdf["buffered"].intersects(brooklyn))

# Q: which points are entirely within the original boroughs' polygons
gdf["within"] = gdf["bufferred_centroid"].within(gdf)
print(gdf["within"])

# 7:08
gdf = gdf.set_geometry("buffered_centroid")
ax = gdf.plot(
    "within", legend=True, categorical=True, legend_kwds={"loc": "upper left"}
)
gdf["boundary"].plot(ax=ax, color="black", linewidth=0.5)


