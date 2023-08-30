# Parquet with Geopandas

Why is it not ready for production?
- it is an early implementation using geoparquet 
- it is not guaranteed to be stable due to potentially large breaking change updates
- so future updates may dramtically alter the way the parquet file is stored


* Any geometry columns present are serialized to WKB format in the file.

WKB:
- Well-Known Binary format
- binary representation used to store geospatial data
- WKT = well known text 
- each component is encoded as a series of bytes
- only supports simple geometries like points, lines and polygons
- 
