import geodatasets
from geopandas import *
import matplotlib.pyplot as plt

# chicago = read_file(geodatasets.get_path("geoda.chicago_commpop"))
# chicago.to_file("data/chicago_commpop.geojson", driver="GeoJSON")

# groceries = read_file(geodatasets.get_path("geoda.groceries"))
# groceries.to_file("data/groceries.geojson", driver="GeoJSON")

chicago = read_file("data/chicago_commpop.geojson")
groceries = read_file("data/groceries.geojson")
# chicago.plot(column="POP2010", legend=True, 
#              legend_kwds={"label": "Population in 2010", 
#                           "orientation": "horizontal"})


# Use the mpl_toolkits to horizontally align the plot axes and the legend axes
# and change the width 

from mpl_toolkits.axes_grid1 import make_axes_locatable 

# fig, ax = plt.subplots(1, 1)
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("bottom", size="5%", pad=0.1)
# chicago.plot(
#     column="POP2010",
#     ax=ax,
#     legend=True,
#     cax=cax,
#     legend_kwds={"label": "Population in 2010", 
#                            "orientation": "horizontal"}
# )


# cmap determines the colors
# chicago.plot(column='POP2010', cmap='OrRd')
# plt.show()

# plotting just the boundaries! 
# chicago.boundary.plot()


"""
You can scale the coloring of maps with the `scheme` option.
Requires that you have `mapclassify` installed.
schemes: box_plot, equal_interval, fisher_jenks ...
"""

# Plotting data with missin values
# import numpy as np 
# # here we set some values to NAN on purpose
# chicago.loc[np.random.choice(chicago.index, 30), 'POP2010'] = np.nan
# chicago.plot(column='POP2010', missing_kwds={'color': 'lightgrey'})
# chicago.plot(
#     column="POP2010",
#     legend=True,
#     scheme="quantiles", 
#     figsize=(15, 10), 
#     missing_kwds={
#         "color": "lightgrey",
#         "edgecolor": "red",
#         "hatch": "///",
#         "label": "Missin values",
#     }
# )
# plt.show()

# removing the axis:
# ax = chicago.plot()
# ax.set_axis_off()
# plt.show()

"""
Maps with Layers!

- when combining maps, make sure they share a common CRS (so they will align)

"""

# you set one plot as the `ax` argument to layer them!
# groceries.plot(marker='*', color='green', markersize=5)
# make them have the same CRS!!!
groceries = groceries.to_crs(chicago.crs)
base = chicago.plot(color="white", edgecolor="black")
groceries.plot(ax=base, marker="o", color="red", markersize=5)
plt.show()

# ^ this should work but it is not! groceries and chicago don't appear to be on 
# the same CRS for some reason

# Note: didn't finish yet.
