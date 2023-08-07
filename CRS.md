# CRS 

Coordinate Reference System.

**Datum** -- the reference system.
**Area of use** -- CRS can be optimized for a specific area of interest.
**Axes and Units** -- longitude and latitude are usually measured in degrees. Units for x, y coordinates are often measured in meters.

How to choose a CRS?
- I think it is often determined by which geographic area you are looking at.
- e.g. in one article they used EPSG:32148, because they were looking at Seattle data.

CRS Codes: https://spatialreference.org/

In GeoPandas you can check for the crs with `df.crs`.  

When the CRS is geographic, the coordinates are in latitude and longitude.  
In those cases, its CRS is WGS84.  
The authority code for WGS84 is `EPSG:4326`.

`EPSG:2263` has coordinates in feet.
To project one CRS to another: `df.to_crs("EPSG:4326")`

!! For operations that rely on **distance** or **area** you always need to use a projected CRS (in meters, feet, kilometers, etc.) not a geographic one (in degrees).  
GeoPandas operations are planar, whereas degrees reflect the position on a sphere. 

#### Sources 

1. https://www.learndatasci.com/tutorials/geospatial-data-python-geopandas-shapely/
2. https://medium.com/@haniszulaikha/starter-tutorial-on-geopandas-d3ede5cc16e9
3. https://geopandas.org/en/stable/getting_started/introduction.html
