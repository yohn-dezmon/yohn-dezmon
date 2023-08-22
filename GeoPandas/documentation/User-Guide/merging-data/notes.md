# Merging Data

You can merge data with `attribute` joins or `spatial` joins.  

#### Attribute joins 

a `GeoSeries` or `GeoDataFrame` is joind with a regular `pandas.Series` or `pandas.DataFrame` based on a common variable.  

* accomplished using the `merge()` method
* the GeoDataFrame must be in the left position, and the DataFrame in the right position

#### Spatial joins 

Observations from two `GeoSeries` or `GeoDataFrame` are combined based on their spatial relationship
to each other.  

