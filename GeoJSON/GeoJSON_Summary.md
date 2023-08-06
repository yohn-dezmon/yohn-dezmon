# GeoJSON


A GeoJSON object may represent a region of space (a Geometry), a spatially bounded entity (a Feature), or a list of Features (a FeatureCollection).

GeoJSON files have the file extension `.geojson`.

Geometry types:
- `Point`, `LineString`, `Polygon`, `MultiPoint`, `MultiLineString`, `MultiPolygon`, and `GeometryCollection`.

`GeometryCollection` can be heterogeneous. 

Example **FeatureCollection**:

```
{
       "type": "FeatureCollection",
       "features": [{
           "type": "Feature",
           "geometry": {
               "type": "Point",
               "coordinates": [102.0, 0.5]
           },
           "properties": {
               "prop0": "value0"
           }
       }, ...
       ]
}
```

A third party data source may return a single `FeatureCollection`, which in turn contains many `Features`. 

A `Feature` can be a `Polygon`, `LineString`, `Point`.

Any GeoJSON object must have the `type` field/member.  
A GeoJSON object may have a bbox (bounding box) field/member.

Geometry Object:
- The value of the type member must be one of the seven geometry types.
- All Geometry objects, except for GeometryCollection, must have a member with the name `coordinates`. Coordinates must be an array. The structure of the coordinates is determined by the Geometry type. Empty coordinates MAY be interpreted as NULL.

Properties:
- within each feature the `properties` object determines the column names and values when you read GeoJSON into a GeoDataframe. The final column will be `geometry` which is determined by the GeoJSON `geometry` field/member. 

#### Questions:

1. FeatureCollection vs. GeometryCollection?

2. What does it mean when a LineString has many arrays of coordinates? (e.g. 4 in the example above)
- those are the points that define the line. Each point is connected by a straight line.

3. How does GeoJSON work with dates? Can a Feature have date properties? How is time
series data organized?


4. What is a MultiPolygon?
- I think these are the gemoetries used to create basemaps?


#### Sources:

1. [GeoJSON RFC](https://datatracker.ietf.org/doc/html/rfc7946) 


#### Licenses:

TODO: get the BSD License or remove/recreate your own examples.
