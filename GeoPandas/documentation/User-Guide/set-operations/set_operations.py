from shapely.geometry import Polygon
from geopandas import GeoSeries, GeoDataFrame
import matplotlib.pyplot as plt

polys_1 = GeoSeries([Polygon([(0,0), (2,0), (2,2), (0,2)]),
                     Polygon([(2,2), (4,2), (4,4), (2,4)])])

polys_2 = GeoSeries([Polygon([(1,1), (3,1), (3,3), (1,3)]),
                              Polygon([(3,3), (5,3), (5,5), (3,5)])])

# what are the df_1 and df_2 columns?
# they are just internal labels so we can easily distinguish the two polygons 
# within each dataframe
df_1 = GeoDataFrame({"geometry": polys_1, "df_1": [1,2]})
print(f"df_1: \n {df_1}")
df_2 = GeoDataFrame({"geometry": polys_2, "df_2": [1,2]})

# ax = df_1.plot(color="red")
# df_2.plot(ax=ax, color='green', alpha=0.5)
# plt.show()

"""
The `overlay()` method will determine the set of all individual geometries from 
overlaying two input GeoDataFrames.
"""

res_union = df_1.overlay(df_2, how="union")

print(res_union)
