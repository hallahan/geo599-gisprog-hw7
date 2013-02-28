#Nicholas Hallahan
#GEO599
#Wed Feb 27 2013
#HW7
#GNU GPLv3 License
#http://en.wikipedia.org/wiki/GNU_General_Public_License

# This is the arcpy interface class!

import sys
import traceback

try:
    # Import arcpy module
    print('importing arcpy...')
    import arcpy
    print('done importing arcpy!')
except Exception, err: 
    raise Exception("UNABLE TO LOAD ARCPY!")

class HW7ArcPy: # class to interface with spatial analyst
    # gets our needed extentions checked out
    def __init__(self, input_dir, intermediate_dir, output_dir):
        self.input_dir = input_dir
        self.intermediate_dir = intermediate_dir
        self.output_dir = output_dir

        ################# INPUT FILES ########################
        # shapefile containing the location of all landslides in oregon
        self.landslides = input_dir + "clipped_slido.shp" 

        # raster containing slope data of oregon
        self.slope = input_dir + "slope"

        # shapefile containing major highways of oregon
        self.highways = input_dir + "Highways.shp"
        ######################################################

        ############### TEMP FILES ############################
        # we need a polygon for calculating the intersection between slides and highway
        self.highways_buffered = intermediate_dir + "highways_buffered.shp"

        # the points of intersection where there were landslides on the highway
        self.intersection = intermediate_dir + "intersection.shp"

        # temporary layer of landslide_road_slope
        self.zonal_stats_layer = intermediate_dir + "zonal_stats_layer"
        ######################################################

        ############## OUTPUT FILES #########################
        # shapefile containing the zonal stats of the slope at that landslide point
        # stats are in the field "GRID_CODE"
        self.landslide_road_slope =  output_dir + "landslide_road_slope.shp"

        # layer converted into a kml file so we can use this data in Google Earth
        self.kmz = output_dir + "landslide_road_slope.kmz"
        #####################################################

        try:
            arcpy.CheckOutExtension("Spatial") # make sure the spatial analyst is checked out
        except Exception, err:
            raise Exception("SPATIAL ANALYST ERROR: You either dont have Spatial Analyst or you need to pay for a license...")
        

    # the actual processing with arcpy
    def createLandslideRoadSlope(self):
        try:
            # Process: Buffer
            # we need a polygon for calculating the intersection between slides and highway
            print("Process: Buffer")
            arcpy.Buffer_analysis(self.highways, self.highways_buffered, "100 Meters", "FULL", "ROUND", "NONE", "")

            # Process: Intersect
            # the points of intersection where there were landslides on the highway
            print("Process: Intersect")
            arcpy.Intersect_analysis([self.highways_buffered, self.landslides], self.intersection, "ALL", "", "INPUT")

            # Process: Near 
            # including landslides that are near the buffer of the highway
            print("Process: Near ")
            arcpy.Near_analysis(self.intersection, self.highways_buffered, "", "NO_LOCATION", "NO_ANGLE")

            # Process: Zonal Statistics
            # raster of the slope at landslide points
            print("Process: Zonal Statistics")
            self.zonal_stats_raster = arcpy.sa.ZonalStatistics(self.intersection, "FID", self.slope, "MEAN", "DATA")

            # Process: Raster to Point
            # stats are in the field "GRID_CODE"
            print("Process: Raster to Point")
            arcpy.RasterToPoint_conversion(self.zonal_stats_raster, self.landslide_road_slope, "Value")

            # Process: Make Feature Layer
            # we need a layer to be able to convert to kml
            print("Process: Make Feature Layer")
            arcpy.MakeFeatureLayer_management(self.landslide_road_slope, self.zonal_stats_layer, "", "", "Shape Shape VISIBLE NONE;FID FID VISIBLE NONE;POINTID POINTID VISIBLE NONE;GRID_CODE GRID_CODE VISIBLE NONE")

            # Process: Layer To KML
            print("Process: Layer To KML")
            arcpy.LayerToKML_conversion(self.zonal_stats_layer, self.kmz, "1", "false", self.landslide_road_slope, "1024", "96", "CLAMPED_TO_GROUND")
            
            print("Success!")
        except Exception, err: # an error occurred (probably in arcGIS)
            print("Sorry, an error has occurred while processing with arcpy:"+format(e))
            exc_type, exc_value, exc_traceback =sys.exc_info()
            print(exc_type)
            print(exc_value)
            traceback.print_tb(exc_traceback, limit=10)
