#Nicholas Hallahan
#GEO599
#Wed Feb 27 2013
#HW7
#GNU GPLv3 License
#http://en.wikipedia.org/wiki/GNU_General_Public_License

import sys
import traceback
from HW7ArcPy import HW7ArcPy

# importing and setting up paths
try:
    import os
    import shutil

    # no args, we just assume everything is in the dir of the script
    cwd = os.getcwd() + "\\"
    if len(sys.argv) is 1:
        input_dir = cwd + "hw7_input\\"
        intermediate_dir = cwd + "hw7_intermediate\\"
        output_dir = cwd + "hw7_output\\"
    # only given directory of input files, output dir will be in cwd
    elif len(sys.argv) is 2:
        input_dir = sys.argv[1]
        if input_dir[-1] != '/' or input_dir[-1] != '\\':
            input_dir = input_dir + '\\'
        intermediate_dir = cwd + "hw7_intermediate\\"
        output_dir = cwd + "hw7_output\\"
        if os.path.isdir(input_dir) is False:
            print "INVALID INPUT DIRECTORY! WE CANT DO THIS..."
            raise IOError 
    # input dir and output dir
    else:
        input_dir = sys.argv[1]
        if input_dir[-1] != '/' or input_dir[-1] != '\\':
            input_dir = input_dir + '\\'
        intermediate_dir = cwd + "hw7_intermediate\\"
        output_dir = sys.argv[2]
        if output_dir[-1] != '/' or output_dir[-1] != '\\':
            output_dir = output_dir + '\\'
        if os.path.isdir(input_dir) is False:
            print "INVALID INPUT DIRECTORY! WE CANT DO THIS..."
            raise IOError 

    
    
    # make sure intermediate and output directories are created and empty
    if os.path.isdir(input_dir) is False:
        print "INVALID INPUT DIRECTORY!"
        raise IOError 
    if os.path.exists(intermediate_dir):
        if len(os.listdir(intermediate_dir)) > 0:
            print("The intermediate directory " + intermediate_dir + " must be empty.")
            print("Please empty this directory and try again.")
            print("Exiting.")
            sys.exit()
    else:
        os.mkdir(intermediate_dir)
        print('Created Empty Dir: ' + intermediate_dir)
    if os.path.exists(output_dir):
        if len(os.listdir(output_dir)) > 0:
            print("The output directory " + output_dir + " must be empty.")
            print("Please empty this directory and try again.")
            print("Exiting.")
            sys.exit()
    else:
        os.mkdir(output_dir)
        print('Created Empty Dir:' + output_dir)

    # create Arc Interface Object
    arc = HW7ArcPy(input_dir, intermediate_dir, output_dir)

    # process
    arc.createLandslideRoadSlope()
    

except Exception as e:
    print("Sorry, an error has occurred:"+format(e))
    exc_type, exc_value, exc_traceback =sys.exc_info()
    print(exc_type)
    print(exc_value)
    traceback.print_tb(exc_traceback, limit=10)

