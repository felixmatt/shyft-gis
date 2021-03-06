import sys
import os

# local imports
HOME= os.environ['HOME']
WORKDIR = HOME+"/shyft-gis"
sys.path.append(WORKDIR)
import process_layers as proc

def setup_exmaple_catchment(DATA_PATH):
    ptp = DATA_PATH # path to polygon
    ptr = DATA_PATH+'/corine_land_cover_2012/' # path to raster
    ptd = DATA_PATH+'/dem/'
    plf = ["12.166_shyft_gridded/12.166_gridded.shp", 
                            "50.2_shyft_gridded/50.2_gridded.shp", 
                            "50.5_shyft_gridded/50.5_gridded.shp", 
                            "50.8_shyft_gridded/50.8_gridded.shp", 
                            "50.10_shyft_gridded/50.10_shyft_gridded.shp", 
                            "50.11_shyft_gridded/50.11_shyft_gridded.shp", 
                            "50.13_shyft_gridded/50.13_gridded.shp", 
                            "50.38_shyft_gridded/50.38_gridded.shp"] # polygon layer files
    
    plf = [ptp + '/' + f for f in plf]

    pcn = ["12.166_centroids", "50.2_centroids", "50.5_centroids", "50.8_centroids", "50.10_centroids", "50.11_centroids", "50.13_centroids", "50.38_centroids"]

    rlf = ["/forest_fraction.tif", 
            "/lake_fraction.tif",
            "/glacier_fraction.tif",
            "/reservoir_fraction.tif"] # raster layer files
    dff = ["dem_finse.tif", "slope_finse.tif", "aspect_finse.tif"] # dem feature files
    finse = proc.catchment_layers("finse", ptp, ptd, ptr, plf, pcn, rlf, dff)
    return finse


DATA_PATH= WORKDIR+'/finse_qgis' # dir with required catchment maps
DATA_INT=DATA_PATH+'/int' # empty dir for intermediate files, must exist
OUTFILE = WORKDIR+'/cell_data.nc' # shyft cell data file

catchment = setup_exmaple_catchment(DATA_PATH)
catchment.copy_files(DATA_INT) # create intermediate files and point them to polygon_layer_files
catchment.calculate_landcover_attributes()
catchment.calculate_topography_attributes()
catchment.create_cell_data_files(OUTFILE)
