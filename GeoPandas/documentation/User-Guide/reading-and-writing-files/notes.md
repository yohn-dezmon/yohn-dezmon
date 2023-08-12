# Reading & Writing Data

`geopandas.read_file()`:
- returns a GeoDataFrame object
- this relies on a library called `fiona`
- you can explicitly set the driver (shapefile, GeoJSON) with the `driver` keyword
- **you can pick a single layer** with the `layer` keyword:
```
countries_gdf = geopandas.read_file("package.gpkg", layer='countries')
```
