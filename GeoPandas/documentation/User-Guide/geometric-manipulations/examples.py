import geopandas 
import geodatasets
from geopandas import GeoSeries 
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

p1 = Polygon([(0,0), (1,0), (1, 1)])
p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
g = GeoSeries([p1, p2, p3])

print(g)
# g.plot()
# plt.show()

# this returns a pandas Series
print(g.area)
"""
0    0.5
1    1.0
2    1.0
dtype: float64
"""

# this returns a GeoSeries
print(g.buffer(0.5))
"""
0    POLYGON ((-0.35355 0.35355, 0.64645 1.35355, 0...
1    POLYGON ((-0.50000 0.00000, -0.50000 1.00000, ...
2    POLYGON ((1.50000 0.00000, 1.50000 1.00000, 1....
dtype: geometry
"""

# nybb_path = geodatasets.get_path('nybb')
boros = geopandas.read_file('data/nybb.geojson')
# boros.to_file('data/nybb.geojson', driver='GeoJSON')

boros.set_index('BoroCode', inplace=True)
boros.sort_index(inplace=True)
# boros.plot()
# plt.show()

convex_hull = boros['geometry'].convex_hull
# convex_hull.plot(cmap='viridis')
# plt.show()

# Generating a GeoSeries with 2000 random points 
import numpy as np 
from shapely.geometry import Point 
xmin, xmax, ymin, ymax = 90000, 1080000, 120000, 280000
xc = (xmax - xmin) * np.random.random(2000) + xmin 
yc = (ymax - ymin) * np.random.random(2000)  + ymin 
pts = GeoSeries([Point(x, y) for x, y in zip(xc, yc)])


# draw a circle with a fixed radius around each point 
circles = pts.buffer(2000)
# collapse the circles into a single MultiPolygon geometry 
mp = circles.unary_union 

# the part of the unioned geometry contained in each borough
holes = boros['geometry'].intersection(mp)
# holes.plot(cmap='viridis')
# plt.show()

# cut out holes where the buffered circles are
# (the points within each borough)
boros_with_holes = boros['geometry'].difference(mp)
boros_with_holes.plot(cmap='viridis')
plt.show()

"""
Difference can also be represented as:
boros.geometry - mp 

I think intersection could be represented with:
boros.geometry & mp
"""

# calculate the fractionanl area in each borough that are in the holes
print(holes.area / boros.geometry.area)

