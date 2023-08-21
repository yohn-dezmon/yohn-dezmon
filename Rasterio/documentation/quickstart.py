import rasterio

dataset = rasterio.open('example.tif')


# 'example.tif'
print(dataset.name)
# 'r' 
print(dataset.mode)
# False
print(dataset.closed)


# 1 -- i.e. there is 1 band
print(dataset.count)

# 7731
print(dataset.width)

# 7871
print(dataset.height)

# {1: 'uint16'}
# it contains 1 band with unsigned 16-bit integer values
print({i: dtype for i, dtype in zip(dataset.indexes, dataset.dtypes)})


# Showing the overall Bounding box of the dataset 
# BoundingBox(left=358485.0, bottom=4028985.0, right=590415.0, top=4265115.0)
print(dataset.bounds)

# this gives us the meters from the origin of the CRS 
# this is the bottom left corner!!! (0, 0)
print(dataset.transform * (0, 0))

# position of the lower right corner
print(dataset.transform * (dataset.width, dataset.height))

# CRS.from_epsg(32612)
print(dataset.crs)


