# GeoJSON


A GeoJSON object may represent a region of space (a Geometry), a spatially bounded entity (a Feature), or a list of Features (a FeatureCollection). 

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
       }, {
           "type": "Feature",
           "geometry": {
               "type": "LineString",
               "coordinates": [
                   [102.0, 0.0],
                   [103.0, 1.0],
                   [104.0, 0.0],
                   [105.0, 1.0]
               ]
           },
           "properties": {

               "prop0": "value0",
               "prop1": 0.0
           }
       }, {
           "type": "Feature",
           "geometry": {
               "type": "Polygon",
               "coordinates": [
                   [
                       [100.0, 0.0],
                       [101.0, 0.0],
                       [101.0, 1.0],
                       [100.0, 1.0],
                       [100.0, 0.0]
                   ]
               ]
           },
           "properties": {
               "prop0": "value0",
               "prop1": {
                   "this": "that"
               }
           }
       }]
   }
```

A third party data source may return a single `FeatureCollection`, which in turn contains many `Features`. 

A `Feature` can be a `Polygon`, `LineString`, `Point`.

Any GeoJSON object must have the `type` field/member.  
A GeoJSON object may have a bbox (bounding box) field/member.

Geometry Object:
- The value of the type member must be one of the seven geometry types.
- All Geometry objects, except for GeometryCollection, must have a member with the name `coordinates`. Coordinates must be an array. The structure of the coordinates is determined by the Geometry type. Empty coordinates MAY be interpreted as NULL.

#### Questions:

1. FeatureCollection vs. GeometryCollection?

2. What does it mean when a LineString has many arrays of coordinates? (e.g. 4 in the example above)


#### Sources:

1. [GeoJSON RFC](https://datatracker.ietf.org/doc/html/rfc7946) 


#### Licenses:

TODO: get the BSD License or remove/recreate your own examples.
