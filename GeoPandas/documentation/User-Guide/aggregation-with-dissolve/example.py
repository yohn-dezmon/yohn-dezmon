import geodatasets 

nepal = geopandas.read_file(geodatasets.get_path('geoda.nepal'))
nepal = nepal.rename(columns={"name_2": "zone"})

