# Missing and empty geometries

**Empty Geometries**:
- geometry objects that have no coordinates
- they have no area
- they can originate from taking the intersection of two non-overlapping polygons
- the scalar object is still a Shapely geometry object

**Missing Geometries**:
- unknown values in a GeoSeries.
- they will be ignored in reductions like `unary_union`
- the scalar object when accessing them is the python `None` object

**propagate**:
- missing geometries will be missing from the result as well after spatial operations
- empty geometries are treated as geometry and the result depends on the operation

```
# POLYGON Empty
Polygon([])
```

```
from shapely.geometry import Polygon
s = geopandas.GeoSeries([Polygon([(0, 0), (1, 1), (0, 1)]), None, Polygon([])])
# 0.5, NaN, 0.0
s.area
```

The `GeoSeries.isna()` method will only check for missing values and not for empty geometries:
```
s.isna()
False
True
False
```

To get the empty geometries use `GeoSeries.is_empty`.

To get non-empty/non-missing geometries, use both:
```
s.is_empty | s.isna()
```

`align` method:
- makes the indicies of two GeoDataFrames match...
- I don't really understand the usecase here still...
- it is used under the hood by `intersection()`


