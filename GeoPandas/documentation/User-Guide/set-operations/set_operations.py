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
# UNION!
# res_union = df_1.overlay(df_2, how="union")
# print(res_union)
# what is cmap='tab10'?
# ax = res_union.plot(alpha=0.5, cmap='tab10')
# # what is edgecolor='k'?
# # what is facecolor='none'?
# df_1.plot(ax=ax, facecolor='none', edgecolor='k')
# df_2.plot(ax=ax, facecolor='none', edgecolor='k')
# plt.show()

# INTERSECTION!
# res_intersection = df_1.overlay(df_2, how="intersection")
# ax = res_intersection.plot(alpha=0.5, cmap='tab10')
# # what is edgecolor='k'?
# # what is facecolor='none'?
# df_1.plot(ax=ax, facecolor='none', edgecolor='k')
# df_2.plot(ax=ax, facecolor='none', edgecolor='k')
# plt.show()

# SYMMETRIC DIFFERENCE!
# res_sym_diff = df_1.overlay(df_2, how="symmetric_difference")
# ax = res_sym_diff.plot(alpha=0.5, cmap='tab10')
# # what is edgecolor='k'?
# # what is facecolor='none'?
# df_1.plot(ax=ax, facecolor='none', edgecolor='k')
# df_2.plot(ax=ax, facecolor='none', edgecolor='k')
# plt.show()

# DIFFERENCE! 
# i.e. the regions in df1 that are not in df2
# res_diff = df_1.overlay(df_2, how="difference")
# ax = res_diff.plot(alpha=0.5, cmap='tab10')
# # what is edgecolor='k'?
# # what is facecolor='none'?
# df_1.plot(ax=ax, facecolor='none', edgecolor='k')
# df_2.plot(ax=ax, facecolor='none', edgecolor='k')
# plt.show()

# Identity 
res_id = df_1.overlay(df_2, how="identity")
ax = res_id.plot(alpha=0.5, cmap='tab10')
# what is edgecolor='k'?
# what is facecolor='none'?
df_1.plot(ax=ax, facecolor='none', edgecolor='k')
df_2.plot(ax=ax, facecolor='none', edgecolor='k')
plt.show()
