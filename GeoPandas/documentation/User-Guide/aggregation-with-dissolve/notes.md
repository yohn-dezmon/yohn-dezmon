# Aggregation with Dissolve 

* spatial data are often more granular than needed.  
e.g. you have data at a sub-national level, but you are interested in data at the country level.  

Downsampling vs. Upsampling:
- 

In non-spatial setting, you can aggregate data using the `.groupby()` functionality of a df.  
In Geopandas you can aggregate **geometric features** using the `dissolve()` function.  

`dissolve()`:
- it "dissolves" the geometries within a group into a single geometric feature (using the `unary_union` method)
- it aggregates all of the rows of data in a group using `groupby.aggregate`
- it combines those two results  


