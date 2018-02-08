import sys
import os
from shutil import copy
from netCDF4 import Dataset

# local imports
HOME= os.environ['HOME']
workdir = HOME+"/Documents/github/shyft-gis"
sys.path.append(workdir)
import process_layers as proc

def setup_finse():
    ptp = DATA_PATH+'shyft_catchments/' # path to polygon
    ptr = DATA_PATH+'shyft_catchments/' # path to raster
    ptd = DATA_PATH+'dem/'
    plf = ["12.166_shyft_gridded/12.166_gridded.shp", 
                            "50.2_shyft_gridded/50.2_gridded.shp", 
                            "50.5_shyft_gridded/50.5_gridded.shp", 
                            "50.8_shyft_gridded/50.8_gridded.shp", 
                            "50.10_shyft_gridded/50.10_shyft_gridded.shp", 
                            "50.11_shyft_gridded/50.11_shyft_gridded.shp", 
                            "50.13_shyft_gridded/50.13_gridded.shp", 
                            "50.38_shyft_gridded/50.38_gridded.shp"] # polygon layer files

    pcn = ["12.166_centroids", "50.2_centroids", "50.5_centroids", "50.8_centroids", "50.10_centroids", "50.11_centroids", "50.13_centroids", "50.38_centroids"]

    rlf = ["g100_clc12_V18_5a/corine_forest_fraction.tif", 
            "g100_clc12_V18_5a/corine_lake_fraction.tif",
            "g100_clc12_V18_5a/corine_glacier_fraction.tif",
            "g100_clc12_V18_5a/corine_reservoir_fraction.tif"] # raster layer files
    dff = ["dem_finse.tif", "slope_finse.tif", "aspect_finse.tif"] # dem feature files
    finse = catchment_layers("finse", ptp, ptr, plf, pcn, rlf, dff)
    return finse

if __name__ == "__main__":

    DATA_PATH= HOME+'/Documents/finse/GIS_data/'
    DATA_INT=DATA_PATH+'shyft_catchments/int'

    finse = setup_finse()
    finse.copy_files(DATA_INT) # create intermediate files and point them to polygon_layer_files
    finse.calculate_means()
    finse.calculate_landcover_attributes():
    finse.calculate_topography_attributes():
