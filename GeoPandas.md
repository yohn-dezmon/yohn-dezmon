# GeoPandas

Polygons are made up of lines. Lines are made up of points.

GeoDataframe.
- A GeoSeries handles the geometries.
- Geometries are in a column to the right of the data.


You can have multiple GeoSeries in a GeoDataframe, but only one 
GeoSeries can be the **active** geometry. 

Active geometry:
- all geometric operations applied to a GeoDataframe operate on this active 
column.
-  When reading in a shapefile or a GeoJSON file, GeoPandas knows which column is a GeoSeries
- it labels this column “geometry”, and automatically set it to the active column.
- GeoDataFrame.set_geometry() can be used to manually set the active column
- GeoDataFrame.geometry -- tells you what the active column is

We'll be dealing with shapefile (.shp) and GeoJSON (.geojson) which 
are file types that can house vector data such as geometric objects
mentioned above.


$ pip install geopandas 



#### Questions:
1. What if there are various geometry columns, how does GeoPandas name them?

2. What does a GeoJSON file look like?



#### Sources:

1. https://www.learndatasci.com/tutorials/geospatial-data-python-geopandas-shapely/

2. https://medium.com/@haniszulaikha/starter-tutorial-on-geopandas-d3ede5cc16e9
