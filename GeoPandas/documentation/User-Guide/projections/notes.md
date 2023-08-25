# Projections

spatialreference.org has the codes of the most commonly used projections.  
A common projection is WGS84.  
The code for WGS84 is `"EPSG:4326"`.  

Common projections and their EPSG codes:
* WGS84 Latitude/Longitude: EPSG:4326
* UTM Zones (North): EPSG:32633
* UTM Zones (South): EPSG:32733


WKT2 is the preferred format to store CRS info. That or SRID.  

2 operations for CRS:
- setting a projection 
- re-projecting  

Most of the time you don't need to load a projection. Data from a reputable source will almost always have projection information.  


To see an object's CRS:  
`gdf.crs`  

If you're loading in data from a spreadsheet with latitude and longitude pairs, there will be no default CRS, so you have to set it!  
```
my_geoseries = my_geoseries.set_crs("EPSG:4326")
my_geoseries = my_geoseries.set_crs(epsg=4326)
```

As of GeoPandas 0.8 you can have different CRS' for different geometry columns.  

`.crs` returns a `pyprojc.CRS` object.  
https://pyproj4.github.io/pyproj/stable/api/crs/crs.html#pyproj.crs.CRS  

These two lines are equivalent: 
```
gdf.crs = "+proj=laea +lat_0=45 +lon_0=-100 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs"
gdf.crs = "EPSG:2163"
```
so use the second line if you know the EPSG code.  

You can find the EPSG code using the `pyproj` library:  
```
impot pyproj 
crs = pyproj.CRS("+proj=laea +lat_0=45 +lon_0=-100 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs")
crs.to_epsg()
```

In GeoPandas coordinaets are always stored in (x, y), i.e. (lon, lat).  


pyproj now honours the axis order of the EPSG definition. However, proj4 strings or older WKT versions don’t specify this correctly, which can be a reason that the CRS object is not equal to the expected EPSG code.  


