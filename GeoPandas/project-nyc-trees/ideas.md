Use a jupyter notebook to do an analysis of a given dataset.
Try to utilize stuff from every aspect of the User Guide.
Maybe use scikit-learn to do some ML (use your notes from the ML course you took).  

* It may be easier to do the points --> lines transformation within PostGIS! 
* Let's try to get PostGIS set up with this project...


### Data Sources
* OpenStreeMap 
* Natural Earth 
* Kaggle (geospatial tag)
* Open Data Portals (cities)
* 

What are some geospatial questions I could analyze with GeoPandas:
1. what % of NYC streets have trees
2. image classification of trees in New York City {this would require satellite/raster images}
3. there are species in the dataset, so we could show in each county, which species is the most common.
4. 


#### General Questions

1. Can you plot a geographic CRS?
- I think so. Geographic CRSs retain the earth's curvature. 
- projected CRSs flatten the earth's surface onto a 2D plane. 
- they can cause distortions as you move away from the equator and Prime Meridian. 
- To mitigate these distortions, especially for more localized maps and analyses, projected CRSs are often used.
- WGS84 is a geographic CRS

2. can we create lines from a bunch of points? If we give each point a buffer, we could try to find the longest lines of trees in NYC! 

