# Reading & Writing Data

`geopandas.read_file()`:
- returns a GeoDataFrame object
- this relies on a library called `fiona`
- you can explicitly set the driver (shapefile, GeoJSON) with the `driver` keyword
- **you can pick a single layer** with the `layer` keyword:
```
countries_gdf = geopandas.read_file("package.gpkg", layer='countries')
```

You can directly download a geojson file from a URL:
```
url = "www.code.net/file.geojson"
df = geopandas.read_file(url)
```

You can load zip files that contain your data
```
zipfile = "zip:///Users/name/Downloads/cb_2017_us_state_500k.zip"
states = geopandas.read_file(zipfile)
```

If the data is within a subfolder of the zip file you have to specify its name:
```
zipfile = "zip:///Path/to/data/here.zip!data"
```

If there are multiple datasets in the same zip file and you only want one, you can do the same as above but for the filename: 
```
!data/file_name.shp
```

You can read in subsets of the geospatial area using a bounding box or geometry. To see how, look at the `geopandas.read_file()` documentation.  

### Geometry Filter

a **mask** is a geographic filter in this case.

```
import geodatasets 

gdf_mask = geopandas.read_file(
    geodatasets.get_path("geoda.nyc")
)
gdf = geopandas.read_file(
    geodatasets.get_path("geoda.nyc education"),
    mask=gdf_mask[gdf_mask.name=="Coney Island"],
)
```

### Bounding box filter 

The bounding box filter only loads data that intersects with the bounding box.

```
# bbox = (left_x, top_y, right_x, bottom_y)
bbox = (
    1031051.7879884212, 224272.49231459625, 1047224.3104931959, 244317.30894023244
)
gdf = geopandas.read_file(
    geodatasets.get_path("nybb"),
    bbox=bbox,
)
```

### Row filter

```
gdf = geopandas.read_file(
    geodatasets.get_path("geoda.nyc"),
    rows=10
)
gdf = geopandas.read_file(
    geodatasets.get_path("geoda.nyc"),
    rows=slice(10, 20),
)
```
... I skipped some of the other filter methods:
* Field/column filters
* SQL WHERE filter


# Writing Spatial Data

in addition to being able to write to various formats, you can also write to a PostGIS db using `gdf.to_postgis()`.  

Shapefile:
```
gdf.to_file("countries.shp")
```

GeoJSON:
```
gdf.to_file("countries.geojson", driver="GeoJSON")
```

GeoPackage:
```
gdf.to_file("package.gpkg", layer="countries", driver="GPKG")
cities_gdf.to_file("package.gpkg", layer="cities", driver="GPKG")
```

# Reading/writing from PostGIS

```
from sqlalchemy import create_engine 
db_url = "postgresql://username:password@host:5432/db"
engine = create_engine(db_url)
gdf.to_postgis("table_name", con=engine)
```


