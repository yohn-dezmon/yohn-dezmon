# Merging Data

You can merge data with `attribute` joins or `spatial` joins.  

#### Attribute joins 

a `GeoSeries` or `GeoDataFrame` is joind with a regular `pandas.Series` or `pandas.DataFrame` based on a common variable.  

* accomplished using the `merge()` method
* the GeoDataFrame must be in the left position, and the DataFrame in the right position

#### Spatial joins 

Observations from two `GeoSeries` or `GeoDataFrame` are combined based on their spatial relationship
to each other.  

`gdf.sjoin()`:
- `predicate` parameter : {intersects, contains, etc.}
    * intersects
    * contains
    * within 
    * touches
    * crosses
    * overlaps
- `how`
    * left 
    * right 
    * inner -- intersect index values and retain only the left_df GeoDataFrame

You can also use `buffer()` to find all the polygons within a given distance of a point. 
- first use `buffer()` to expand each point into a circle of appropriate radius
- intersect those buffered circles with the polygons in question 

`gdf.sjoin_nearest()`:
- joins based on proximity, with the ability to set a maximum search radius
- `max_distance`: specifies the maximum search radius for matching geometries. This can have a significant performance impact, so it is something that should be specified if possible. 
- `distance_col`: a new column is added to the resultant GeoDataFrame with the distances between an input geometry and the nearest geometry 


