# Indexing and selecting data 

Label based indexing with `loc`. Integer based indexing with `iloc`.  
Coordinate based indexing with `cx`!!!  
- slices using a bounding box 
- geometries in the GeoDataFrame or GeoSeries that intersect the box will be returned.  


cx: 
- `.cx[xmin:xmax, ymin:ymax]`
- `.cx[:, :]` will return the entire series 

