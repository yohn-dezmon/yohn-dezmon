# Python Quickstart

GeoTIFF (file format) is used for this tutorial.  
`.tif` is the file extension for GeoTIFF.  

A **dataset band** is an array of values representing the partial distribution of a single variable in 2D space.  
All band arrays of a dataset have the same number of rows and columns.  
The variable represented by the example dataset's sole band is Level-1 digital numbers (DN).  

Some dataset attributes expose the properties of all dataset bands via a tuple of values, one per band.  
To get a mapping of band indexes to variable data types, apply a dictionary comprehension to the `zip()` product of a dataset's DatsetReader.indexes and DatasetReader.dtypes attributes. 

### Dataset georeferencing

A GIS raster dataset's elements/pixels are mapped to regions on the earth's surface.  
Every pixel of a dataset is contained within a spatial bounding box.  
This differs from a typical image file.  


The value of `DatasetReader.bounds` attribute is dervied from the dataset's geospatial **transform**.  
A dataset's `DatasetReader.transform` is an affine transformation matrix that maps pixel locations in (col, row) coordinates to (x, y) spatial positions.  
The product of this matrix and (0, 0) -- the column and row coordinates of the upper left corner of the dataset -- is the spatial position of the upper left corner.  

Between the `DatasetReader.crs` and `DatasetReader.transform` attributes, the georeferencing of a raster dataset is described and the dataset can compared to other GIS datasets.


