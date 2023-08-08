# Time and Geospatial Datasets

If you have a data source that periodically provides you with GeoJSON data representing 
a given region, how do data providers typically deal with dates? Are dates 
included within the GeoJSON or how does that work?

Time can be stored as an attribute (feature classes, mosaic datasets, raster catalogs, tables, etc).  
Or, it can be stored internally, like with `netCDF` or `tracking layers`.

### Feature Layers

* The shape and location of each feature is constant over time but attribute values can change over time 
* The shape and location of each feature changes over time.

**features that change in shape or location over time have to be stored as separate features**.  
(e.g. for hurricane tracks)

On the other hand, if you want to represent population data, you can have different 
rows for each population value over time, but the geometric columns remain the same.  
(hm but this introduces duplication, so it would be better to store the geometric 
data in a separate table, and have an ID to reference it).  
- another example of this format, is for temperature data. 




#### Sources:

1. https://desktop.arcgis.com/en/arcmap/latest/map/time/how-time-is-supported-in-spatial-data.htm
2. https://pro.arcgis.com/en/pro-app/latest/help/mapping/time/how-time-is-supported-in-spatial-data.htm

