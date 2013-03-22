# Usage

Make sure you have set your python path to be the python executable that ArcGIS uses!

You may just run the tool with no args if you have the hw7_input directory in the same place as the script:
```
python hw7.py
```

If you want to specify a specific location where you want to process input files from:
```
python hw7.py C:\exact\path\to\dir
```

If you want to specify both the input and the output directory:
```
python hw7.py C:\exact\path\to\input_dir C:\exact\path\to\output_dir
```

Intermediate files are placed in a directory called `hw7_intermediate` in the directory of the script.

Make sure that the intermediate and output directories are empty. The tool will exit if you have contents in these directories.

# Outputs

You will have a shapefile and a kml file of all of the points on major highways in Oregon that have had landslides. The slope of the terrain at that point is in the field `GRID_CODE`.

# Overview

The purpose of this tool is to the get a polyline feature layer(highway shape file for this assignment)and to buffer the distance with 200 m from the freature layer

Geoprocessing is applied, intersection for this example, and for any point feature meeting in the buffered zone. Such points are taken away separately and distance between the road and the landslide events are computed using mathematical function (Near). The same is updated with the point file.

Zonal statistics is used to find the corresponding value of those active landslides which are in the buffered distance of 200 m, and the raster is further converted in to point feature. It can be exported in to KML for any internet based earth browsers.

3D analyst and spatial analyst tools should be available. It is necessary to have all the input layers in the same projection system model parameters are defined while making this model.

# Contributors

This homework was completed in conjunction with Rubini Mahalingam. The input files were created by Rubini.

# License

GNU GPLv3 License
http://en.wikipedia.org/wiki/GNU_General_Public_License 
