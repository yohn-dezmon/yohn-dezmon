# GeoPandas

Polygons are made up of lines. Lines are made up of points.

GeoDataframe.
- A GeoSeries handles the geometries.
- Geometries are in a column to the right of the data.


You can have multiple GeoSeries in a GeoDataframe, but only one 
GeoSeries can be the **active** geometry. 

Active geometry:
- All geometric operations applied to a GeoDataframe operate on the active 
column.
- When reading in a shapefile or a GeoJSON file, GeoPandas knows which column is a GeoSeries.
- It labels this column `geometry`, and automatically sets it to the active column.
- `GeoDataFrame.set_geometry()` can be used to manually set the active column.
- `GeoDataFrame.geometry` -- tells you what the active column is.

Shapefile (.shp) and GeoJSON (.geojson) are file types that can house vector data.

#### How to install GeoPandas

```
$ pip install geopandas 
```

4 main geometric attributes for `GeoSeries`:
1. `Area` (for polygons/multipolygons) --  `df.area`
2. `Boundary` (for polygons/multipolygons) -- `df.boundary`
3. `Centroid` -- returns the center of a polygon `df.centroid`
4. `Distance` -- `df.distance(geometry)` -- often used in combination with centroid.  
e.g. you would get the centroid of one row's geometry, then calculate the distance to the centroids of all other rows.

Other [geometric operations](https://geopandas.org/en/stable/docs/user_guide/geometric_manipulations.html).


Filtering spatial data:
1. `within()` -- checks if a point is within a polygon
2. `contains()` -- checks if a polygon contains a point


```
points_within_poly = df_1[df_1.geometry.within(df_2['geometry'][0])]
```

```
mask = [df_1['geometry'][0].contains(x) for x in df_2['geometry']]
points_within_poly = df_1[mask]
```

#### Plotting using GeoPandas

```
df_1.plot(figsize=(10, 15), alpha=0.5, edgecolor='k')

for idx, row in df_1.iterrows():
    plt.annotate(text=['area'], xy=(row['centroid'].x, row['centroid'].y), 
        horizontalalignment='center', color = 'k')
```

* adding basemaps... (ensure the basemap uses the same CRS)
* interactive maps (`explore()`) -- `folium.Map`



#### Questions:
1. What if there are various geometry columns, how does GeoPandas name them?

2. What does a GeoJSON file look like?

3. MULTILINESTRING vs. LINESTRING?

4. does `df.centroid` return the center of a line? How is that determined?


#### Sources:

1. https://www.learndatasci.com/tutorials/geospatial-data-python-geopandas-shapely/

2. https://medium.com/@haniszulaikha/starter-tutorial-on-geopandas-d3ede5cc16e9
