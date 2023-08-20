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

### Affine Transformations

`.affine_transform(self, matrix)`:
- transform the geometries of the GeoSeries using an affine transformation matrix 

`.rotate(self, angle, origin='center', use_radians=False)`:
- rotate the coordinates of the GeoSeries 

`.scale(self, xfact=1.0, yfact=1.0, zfact=1.0, origin='center')`:
- scale geometries of the GeoSeries along each (x,y,z) dimension 

`skew(self, angle, origin='center', use_radians=False)`:
- shear/skew the geometries of the GeoSeries by angles along x and y dimensions 

`translate(self, xoff=0.0, yoff=0.0, zoff=0.0)`:
- shift the coordinates of the GeoSeries 


#### Sources:

1. https://geopandas.org/en/stable/docs/user_guide/geometric_manipulations.html
