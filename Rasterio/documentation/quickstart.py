import rasterio

dataset = rasterio.open('example.tif')

# 1 -- i.e. there is 1 band
print(dataset.count)

