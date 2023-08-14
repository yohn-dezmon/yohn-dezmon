from geodatasets import get_path
from geopandas import read_file

# chile = read_file(get_path('geoda.chile_labor'))
# chile.to_file("data/chile_labor.geojson" , driver="GeoJSON")

chile = read_file("data/chile_labor.geojson")
print(chile)
