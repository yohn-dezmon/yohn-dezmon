"""
A GeoSeries is a vector where each entry in the vector is a set of shapes 
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
"""
