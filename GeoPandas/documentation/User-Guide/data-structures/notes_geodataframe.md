# GeoDataFrame 

The `geometry` column, no matter its name, can always be accessed through the `geometry` attribute, e.g. `gdf.geometry`.
Its name can be found by using `gdf.geometry.name`.
To change which column is the active geometry, use `GeoDataFrame.set_geometry()`  

When you read in a geospatial file with `read_file` Geopandas will convert the geomtries into shapely objects and store them in a column called `"geometry"`.

`geopandas.options`:
- `.display_precision`: can control the number of decimals to show in the display of coordinates in the geometry column.  
- 
