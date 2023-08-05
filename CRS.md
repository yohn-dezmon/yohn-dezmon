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




#### Sources 

1. https://www.learndatasci.com/tutorials/geospatial-data-python-geopandas-shapely/
2. https://medium.com/@haniszulaikha/starter-tutorial-on-geopandas-d3ede5cc16e9
