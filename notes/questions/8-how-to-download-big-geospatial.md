For example, the data at this website is huge.

https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/pi5s-9p35

how do I get it?

it is 617 MB
it took like 2 mins to download.

How to speed up loading a large geospatial GeoJSON file into memory with `read_file()`?
- you can use `simplify()` to reduce the precision of geometries 
- you can filter for the features you want to consider, using the `query` parameter
- you can use `dask` for parallel processing! 
- you could set up postgres and utilize PostGIS
 

## Speeding up reading of geospatial data
- https://dev.to/spara_50/speeding-up-geo-data-processing-ig7
- using `pickle` & `pyogrio` wow! 
- 

hm... maybe it would be faster if I were reading this from parquet?
But how do I convert the GeoJSON file into parquet in the first place?

Apparently there is a file format called `geoparquet`! cool.
* can you store files in geoparquet using geopandas?

Parquet can be used to store geospatial data, but it uses `wkb` or `wkt` to store geospatial data objects.

https://blog.dask.org/2017/09/21/accelerating-geopandas-1
- Cython and Dask
- hm these articles don't mention anything about read_file()

