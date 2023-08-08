# Set Operations with Overlay

When working with multiple `polygon` or `line` datasets, users often wish to create 
new shapes based on places where those datasets overlap (or don't overlap).  
You can refer to this manipulations using the language of **sets**.

* intersections: overlapping portion of two shapes
* unions: a new shape covering all of the area of the shapes in provided to the union function.
* differences: the part from one shape that does not overlap with another
* symetrical difference: the part from either shape that does not overlap with the other

^ these types of operations are made available with the GeoPandas library through the 
`overlay()` method.

**overlays** operate at the **DataFrame** level, not on individual geometries. 
i.e. for every shape in the left GeoDataframe, this operation is executed against 
every other shape in the right GeoDataframe (cross-join).




