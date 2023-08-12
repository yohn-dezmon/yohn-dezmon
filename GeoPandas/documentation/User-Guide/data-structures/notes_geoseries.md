# GeoSeries
A GeoSeries is a vector where each entry in the vector (1D array) is a set of shapes 
corresponding to one observation.

A MultiPolygon could be the many polygons that make up the state of Hawaii for example.

3 classes of geometric objects (`shapely` objects)
* Points / Multi-points
* Lines / Multi-lines
* Poyogns / Multi-Polygons

What is a multi-point?
what is a multi-line?
^ apparently these make things more efficient if you're doing geospatial 
operations on a large quantity of points/lines/polygons.

`area` -- shape area (units of projection)
`bounds` -- tuple of max and min coordinates on each axis for each shape
`total_bounds` -- tuple of max and min coordinates on each axis for entire GeoSeries
`geom_type`: type of geometry
`is_valid`: tests if coordinates make a shape that is a reasonable geometric 
shape according to the Simple Feature Access standard.

Basic methods:
- `distance(other)` -- returns a Series of minimum distances from 
- `centroid` -- returns GeoSeries centroids 
- `representative_point()` -- returns GeoSeries of points that are guaranteed to be within each geometry. Tt does NOT return centroids (why?)
Ah, because... a centroid isn't necessarily an existing point within a geometry, it is just the average of the coordinates of all the points that make up the shape.
A representative point is similar to a centroid, but doesn't have an exact mathematical definition, it may be determined by minimizing the distance to all the other points, or trying to balance the distribution of points within the geometry. And the method used is determined by the geometry itself.
- `to_crs()` change coordinate reference system
- `plot()` plot GeoSeries

Relationship tests:
- `geom_almost_equals()`: the shape almost the same as `other` (good when floating point precision issues make shapes slightly different)
- `contains()`: is the shape contained within `other`
- `intersects()`: does the shape intersect `other`



