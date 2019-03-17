#!/usr/bin/env python
"""Reads .
This is a long, multiline description
"""

#########################
##    IMPORT MODULES   ##
#########################
import sys
import glob
import os #we use os.path
import subprocess

#########################
##      HEADER         ##
#########################
__author__ = "Pedro Marques Ferreira da Silva"
__date__ = "March 2019"
__credits__ = ["Pedro Marques Ferreira da Silva"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Silva"
__email__ = "silva.mfpedro@gmail.com"
__status__ = "Development"


#########################
## FUNCTION DEFINITION ##
#########################

#########################
##  GLOBAL VARIABLES   ##
#########################

#Taken from https://github.com/SIlvaMFPedro/python_scripts/wiki/List-of-atlas-repositories
urls = ["https://github.com/SIlvaMFPedro/atlascar_base",
        "https://github.com/SIlvaMFPedro/augmented_perception",
        "https://github.com/SIlvaMFPedro/colormap",
        "https://github.com/SIlvaMFPedro/free_space_detection",
        "https://github.com/SIlvaMFPedro/human_driver_monitor",
        "https://github.com/SIlvaMFPedro/image_labelling",
        "https://github.com/SIlvaMFPedro/kfilter",
        "https://github.com/SIlvaMFPedro/lidar_segmentation",
        "https://github.com/SIlvaMFPedro/laser",
        "https://github.com/SIlvaMFPedro/mtt",
        "https://github.com/SIlvaMFPedro/navigation_msgs",
        "https://github.com/SIlvaMFPedro/odometer",
        "https://github.com/SIlvaMFPedro/rqt_bag",
        "https://github.com/SIlvaMFPedro/tcp_client",
        "https://github.com/SIlvaMFPedro/topic_priority"]

#Can be changed with command line argument clone, i.e., ./pull_all.py clone
clone_mode = False

##########
## MAIN ##
##########

if __name__ == "__main__":

    #--------------------#
    ### Initialization ###
    #--------------------#

    if len(sys.argv)>1:
        if sys.argv[1] == "clone":
            clone_mode = True
        else:
            clone_mode = False

    path = "../"

    #--------------------#
    ###   Clone mode   ###
    #--------------------#
    if clone_mode:
        print "*** Clone mode selected *** " 
        print "Cloning reps to path ../" 

        for url in urls:

            print url
            name = url.split("/")[-1][:-4]

            files = sorted(glob.glob(path + name)) 

            if not len(files) == 0:
                print "Repository " + name + " already exists in " + path + " , will not clone"
            else:
                cmd = "cd " + path + " && git clone " + url
                print "git clone " + url
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    print line,
                    retval = p.wait()


    else:

        print "pulling all reps from path ../" 

        #List all reps, i.e., folders starting by rws2019
        rep_paths = sorted([os.path.join(path,o) for o in os.listdir(path) if os.path.isdir(os.path.join(path,o)) and 'rws' in o])
        #print rep_paths

        for rep_path in rep_paths:
            cmd = "cd " + rep_path + " && git pull"
            print "git pull " + rep_path
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print line,
                retval = p.wait()


    sys.exit()
