Can you plot both a projected and geographic CRS?
- yes. (with geopandas).

Geographic CRS:
- based on longitude and latitude. 
- e.g. WGS84
- plotting shouldn't invovle any issues
- good for global datasets.
- if you use area, the unit would be square degrees, which often doesn't make sense.

Projected CRS:
- dervied from geographic CRSs.
- flatten the surface onto 2D plane. 
- better for calculating area measurements! Can be in feet for example, so area would be ft^2


