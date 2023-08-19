# Geometric Manipulations

The manipulations originate from the Shapely library.  

### Constructive Methods

`.buffer(distance, resolution=16)`:
- return a GeoSeries of geometries representing all points within a given distance of each geometric object.

`.boundary`:
- return a GeoSeries of lower dimensional objects representing each geometry's set-theoretic boundary.  

`.centroid`:
- returns a GeoSeries of points for each geometric centroid.  

`.convex_hull`:
- the smallest convex Polygon containing all the points in each object unless the number of points in the object is less than three. 
- for two points, the convex hull collapses to a LineString
- for 1, a Point

`.envelope`:
- return a GeoSeries of geometries representing the point of smallest rectangular polygon (with sides parallel to the coordinate axes) that contain each object.

`simplify`:
- a GeoSeries of a simplified representation of each object.

`.unary_union`:
- return a geometry containing the union of all geometries in the GeoSeries.




#### Sources:

1. https://geopandas.org/en/stable/docs/user_guide/geometric_manipulations.html
