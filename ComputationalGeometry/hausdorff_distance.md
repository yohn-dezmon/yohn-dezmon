# Hausdorff Distance

The furthest distance that a point on either geometry can be from the nearest point to it on the other geometry.

Shapely:
```
object.hausdorff_distance(other_object)
```

Hausdorff distance gives an interesting measure of their mutual proximity, by indicating the maximal distance between any point of one polygon to the other polygon. Better than the shortest distance, which applied only to one point of each polygon, irrespective of all other points of the polygons.

Take the smallest epsilon where epsilon is the degree of scaling either X or Y, 
such that Y contains all of X and X contains all of Y (when they are respectively
thickened one at a time). In the same "metric space". 

First you find the distance from each point on one line to the nearest point on the other line.  
Then you take the max distance of all of those distances.

#### Sources

1. http://cgm.cs.mcgill.ca/~godfried/teaching/cg-projects/98/normand/main.html#:~:text=Hausdorff%20distance%20gives%20an%20interesting,other%20points%20of%20the%20polygons.

2. https://shapely.readthedocs.io/en/stable/manual.html#geometric-objects

3. https://youtu.be/tvbkSt_QxnE

