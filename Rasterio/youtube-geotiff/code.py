import ratserio
from rasterio.plot import show
from matplotlib import pyplot as plt 

img = rasterio.open('images/MOS_CZ_KR_250.tif')
show(img)

# there are 3 bands 
# this also shows you the shape of the image
full_img = img.read()
